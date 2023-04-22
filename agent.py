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
    
def set_possible_action_q_vals(state, agent, q_table, actions):
  if agent == 'm':
    return q_table.find_q_vals(state.representation['male_position']['cell_type'], actions)
  else:
    return q_table.find_q_vals(state.representation['female_position']['cell_type'], actions)
    
def main():
    env = environment.Environment()
    world_state = state.State(env.environment)
    q_table = qtable.Qtable()
    agent = Agent('m')
    actions = set_possible_actions(world_state, agent.type)
    print('actions ', actions)
    cells = set_possible_cells(world_state, agent.type, actions)
    print('cells ', cells)
    q_vals = set_possible_action_q_vals(world_state, agent.type, q_table, actions)
    print('q_vals ', q_vals)
    chosen_action = policy.pRandom(agent.carrying, cells)
    print('chosen_action ', chosen_action)
    # chosen_action = policy.pExploit(agent.carrying, cells, q_vals)
    # print('chosen_action ', chosen_action)
    # chosen_action = policy.pGreedy(agent.carrying, cells, q_vals)
    # print('chosen_action ', chosen_action)
    next_pos_actions = set_next_position_possible_actions(world_state, agent.type, chosen_action)
    print('next_pos_actions ', next_pos_actions)
    q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, cells[chosen_action], next_pos_actions, 0.2, 0.6)
    print(q_table.table)
    

if __name__ == "__main__" :
    main();