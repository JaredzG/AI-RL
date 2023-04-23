import environment
import state
import agent
import policy
import action
import reward
import value
import qtable

def run_exp3(rl_method, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha, gamma):
  for i in range(10000):
    chosen_policy = ''
    chosen_agent = None
    if i < 500:
      chosen_policy = policy1
    else:
      chosen_policy = policy2
    if i % 2 != 0:
      chosen_agent = m_agent
    else:
      chosen_agent = f_agent
    layer = ''
    match chosen_agent.carrying:
      case True:
        layer = 'carrying'
      case False:
        layer = 'not_carrying'
    actions = agent.set_possible_actions(world_state, chosen_agent.type)
    cells = agent.set_possible_cells(world_state, chosen_agent.type, actions)
    q_vals = agent.set_possible_action_q_vals(world_state, chosen_agent.type, q_table, actions, layer)
    chosen_action = agent.choose_action(chosen_agent, cells, q_vals, chosen_policy)
    next_pos_actions = agent.set_next_position_possible_actions(world_state, chosen_agent.type, chosen_action)
    next_pos_cells = agent.set_next_position_possible_cells(world_state, cells[chosen_action]['coords'], next_pos_actions)
    future_carrying = False
    if (rl_method == 'sarsa'):
      future_carrying = agent.determine_future_carrying(chosen_agent, cells, chosen_action)
    q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, layer, cells[chosen_action]['type'], next_pos_actions, alpha, gamma, rl_method, chosen_policy, future_carrying, next_pos_cells)
    if chosen_agent.type == 'm':
      world_state.update_environment_and_state(world_state.representation['male_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    else:
      world_state.update_environment_and_state(world_state.representation['female_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
      agent.pickup_or_dropoff(chosen_agent, cells[chosen_action]['type'])
    terminal_state_reached = True
    for cell in world_state.representation['dropoff_cell_blocks']:
      if world_state.representation['dropoff_cell_blocks'][cell] < 5:
        terminal_state_reached = False
    if terminal_state_reached:
      env = environment.Environment()
      world_state = state.State(env)
  for x in range(3):
    print('Level', x)
    for y in range(3):
      print('\tRow', y)
      for z in range(3):
        print('\t\tColumn', z, world_state.environment[x][y][z])
  print()
  for layer in ['carrying', 'not_carrying']:
    print(layer)
    for position in ['normal', 'risky', 'pickup', 'dropoff']:
      print('\t', position)
      for action in ['up', 'down', 'left', 'right', 'forward', 'backward']:
        print('\t\t', action, q_table.table[layer][position][action])
  print()
    
def main():
  rl_method = 'q_learning'
  policy1 = 'p_random'
  policy2 = 'p_exploit'
  env = environment.Environment()
  world_state = state.State(env)
  q_table = qtable.Qtable()
  m_agent = agent.Agent('m')
  f_agent = agent.Agent('f')
  alpha1 = 0.3
  alpha2 = 0.1
  alpha3 = 0.5
  gamma = 0.5
  print('experiment 3 -- alpha = 0.3 -- environment and q-table:')
  run_exp3(rl_method, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha1, gamma)
  print('experiment 3 -- alpha = 0.1 -- environment and q-table:')
  run_exp3(rl_method, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha2, gamma)
  print('experiment 3 -- alpha = 0.2 -- environment and q-table:')
  run_exp3(rl_method, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha3, gamma)
  
if __name__ == "__main__" :
    main();