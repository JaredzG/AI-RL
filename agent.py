import action
import qtable
import state
import environment
import policy
class Agent:
  def __init__(self, type, carrying = False):
    self.type = type
    self.carrying = carrying
    
  def toggle_carrying(self):
    self.carrying = not self.carrying
    
def set_possible_actions(state, agent):
  return action.find_possible_actions(state, agent)

def get_new_coords(state, agent, move):
  new_coords = []
  if agent == 'm':
    old_coords = state.representation['male_position']['coords']
  else:
    old_coords = state.representation['female_position']['coords']
  match move:
    case 'up':
      new_coords = [old_coords[0] + 1, old_coords[1], old_coords[2]]
    case 'down':
      new_coords = [old_coords[0] - 1, old_coords[1], old_coords[2]]
    case 'backward':
      new_coords = [old_coords[0], old_coords[1] + 1, old_coords[2]]
    case 'forward':
      new_coords = [old_coords[0], old_coords[1] - 1, old_coords[2]]
    case 'right':
      new_coords = [old_coords[0], old_coords[1], old_coords[2] + 1]
    case 'left':
      new_coords = [old_coords[0], old_coords[1], old_coords[2] - 1]
  return new_coords

def set_next_position_possible_actions(state, agent, move):
  new_coords = get_new_coords(state, agent, move)
  return action.find_next_position_possible_actions(new_coords)
  
def set_possible_cells(world_state, agent, actions):
  return state.find_possible_cells(world_state, agent, actions)

def set_next_position_possible_cells(world_state, coords, actions):
  return state.find_next_position_possible_cells(world_state, coords, actions)
    
def set_possible_action_q_vals(state, agent, q_table, actions):
  if agent == 'm':
    return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions)
  else:
    return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions)
    
def pickup_or_dropoff(agent, position):
  if (position == 'pickup' and agent.carrying == False) or (position == 'dropoff' and agent.carrying == True):
    agent.toggle_carrying()
    
def choose_action(agent, cells, q_vals, chosen_policy = 'p_random'):
  match chosen_policy:
    case 'p_random':
      return policy.p_random(agent.carrying, cells)
    case 'p_exploit':
      return policy.p_exploit(agent.carrying, cells, q_vals)
    case 'p_greedy':
      return policy.p_greedy(agent.carrying, cells, q_vals)
    
def determine_future_carrying(agent, cells, action):
  if (cells[action]['type'] == 'pickup' and cells[action]['is_empty'] == False and agent.carrying == False) or (cells[action]['type'] != 'dropoff' and agent.carrying):
    return True
  return False
    
def main():
  rl_method = 'sarsa'
  chosen_policy = 'p_greedy'
  env = environment.Environment()
  #Initialize state with environment object
  world_state = state.State(env)
  q_table = qtable.Qtable()
  agent = Agent('m')
  actions = set_possible_actions(world_state, agent.type)
  print('actions ', actions)
  cells = set_possible_cells(world_state, agent.type, actions)
  print('cells ', cells)
  q_vals = set_possible_action_q_vals(world_state, agent.type, q_table, actions)
  print('q_vals ', q_vals)
  chosen_action = choose_action(agent, cells, q_vals, chosen_policy)
  print('chosen_action ', chosen_action)
  next_pos_actions = set_next_position_possible_actions(world_state, agent.type, chosen_action)
  print('next_pos_actions ', next_pos_actions)
  next_pos_cells = set_next_position_possible_cells(world_state, cells[chosen_action]['coords'], next_pos_actions)
  print('next_pos_cells ', next_pos_cells)
  future_carrying = False
  if (rl_method == 'sarsa'):
    future_carrying = determine_future_carrying(agent, cells, chosen_action)
  q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, cells[chosen_action]['type'], next_pos_actions, 0.2, 0.6, rl_method, chosen_policy, future_carrying, next_pos_cells)
  print(q_table.table)
  if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
    pickup_or_dropoff(agent, cells[chosen_action]['type'])
  print('agent carrying', agent.carrying)
  if agent.type == 'm':
    world_state.update_environment_and_state(world_state.representation['male_position']['coords'], chosen_action, agent.type, agent.carrying, cells[chosen_action]['type'])
  else:
    world_state.update_environment_and_state(world_state.representation['female_position']['coords'], chosen_action, agent.type, agent.carrying, cells[chosen_action]['type'])
  print('new environment:')
  for x in range(3):
    print(f'Level {x}\n')
    for y in range(3):
      print(f'Row {y}\n')
      for z in range(3):
        print(world_state.environment[x][y][z])
    

if __name__ == "__main__" :
    main();