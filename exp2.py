import environment
import state
import agent
import qtable
def run_exp2(rl_method1, rl_method2, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha, gamma):
  first_dropoff_cell_filled = False
  first_terminal_state_reached = False
  for i in range(10000):
    chosen_rl_method = ''
    chosen_policy = ''
    chosen_agent = None
    if i < 500:
      chosen_rl_method = rl_method1
      chosen_policy = policy1
    else:
      chosen_rl_method = rl_method2
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
    if (chosen_rl_method == 'sarsa'):
      future_carrying = agent.determine_future_carrying(chosen_agent, cells, chosen_action)
    q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, layer, cells[chosen_action]['type'], next_pos_actions, alpha, gamma, chosen_rl_method, chosen_policy, future_carrying, next_pos_cells)
    if chosen_agent.type == 'm':
      world_state.update_environment_and_state(world_state.representation['male_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    else:
      world_state.update_environment_and_state(world_state.representation['female_position']['coords'], chosen_action, chosen_agent.type, chosen_agent.carrying, cells[chosen_action]['type'])
    if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
      agent.pickup_or_dropoff(chosen_agent, cells[chosen_action]['type'])
      
    if first_dropoff_cell_filled == False:
      for cell in world_state.representation['dropoff_cell_blocks']:
        if world_state.representation['dropoff_cell_blocks'][cell] == 5:
          first_dropoff_cell_filled = True
          print('first dropoff cell filled', cell)
          print('q_table:')
          for layer in ['carrying', 'not_carrying']:
            print(layer)
            print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('left'), '{:^15}'.format('right'), '{:^15}'.format('forward'), '{:^15}'.format('backward'))
            for position in ['normal', 'risky', 'pickup', 'dropoff']:
              print('{:^10}'.format(position), '{:^15}'.format(q_table.table[layer][position]['up']), '{:^15}'.format(q_table.table[layer][position]['down']), '{:^15}'.format(q_table.table[layer][position]['left']), '{:^15}'.format(q_table.table[layer][position]['right']), '{:^15}'.format(q_table.table[layer][position]['forward']), '{:^15}'.format(q_table.table[layer][position]['backward']))
            print()
          print()
          break
        
    terminal_state_reached = True
    for cell in world_state.representation['dropoff_cell_blocks']:
      if world_state.representation['dropoff_cell_blocks'][cell] < 5:
        terminal_state_reached = False
    if terminal_state_reached:
      if first_terminal_state_reached == False:
        first_terminal_state_reached = True
        print('first terminal state reached')
        print('q_table:')
        for layer in ['carrying', 'not_carrying']:
          print(layer)
          print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('left'), '{:^15}'.format('right'), '{:^15}'.format('forward'), '{:^15}'.format('backward'))
          for position in ['normal', 'risky', 'pickup', 'dropoff']:
            print('{:^10}'.format(position), '{:^15}'.format(q_table.table[layer][position]['up']), '{:^15}'.format(q_table.table[layer][position]['down']), '{:^15}'.format(q_table.table[layer][position]['left']), '{:^15}'.format(q_table.table[layer][position]['right']), '{:^15}'.format(q_table.table[layer][position]['forward']), '{:^15}'.format(q_table.table[layer][position]['backward']))
          print()
        print()
      env = environment.Environment()
      world_state = state.State(env)
  print('final environment')
  for x in range(2, -1, -1):
    print('Level', x + 1)
    for y in range(2, -1, -1):
      print('{:^60}'.format(str(world_state.environment[x][y][0])), '{:^60}'.format(str(world_state.environment[x][y][1])), '{:^60}'.format(str(world_state.environment[x][y][2])))
  print()
  print('final q-table')
  for layer in ['carrying', 'not_carrying']:
    print(layer)
    print('{:^10}'.format(' '), '{:^15}'.format('up'), '{:^15}'.format('down'), '{:^15}'.format('left'), '{:^15}'.format('right'), '{:^15}'.format('forward'), '{:^15}'.format('backward'))
    for position in ['normal', 'risky', 'pickup', 'dropoff']:
      print('{:^10}'.format(position), '{:^15}'.format(q_table.table[layer][position]['up']), '{:^15}'.format(q_table.table[layer][position]['down']), '{:^15}'.format(q_table.table[layer][position]['left']), '{:^15}'.format(q_table.table[layer][position]['right']), '{:^15}'.format(q_table.table[layer][position]['forward']), '{:^15}'.format(q_table.table[layer][position]['backward']))
    print()
  print()

def main():
  rl_method1 = 'q_learning'
  rl_method2 = 'sarsa'
  policy1 = 'p_random'
  policy2 = 'p_exploit'
  env = environment.Environment()
  world_state = state.State(env)
  q_table = qtable.Qtable()
  m_agent = agent.Agent('m')
  f_agent = agent.Agent('f')
  alpha = 0.3
  gamma = 0.5
  print('experiment 2 environment and q-table:')
  run_exp2(rl_method1, rl_method2, policy1, policy2, env, world_state, q_table, m_agent, f_agent, alpha, gamma)
  
if __name__ == "__main__" :
    main();