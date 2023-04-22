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
  
def set_possible_cells(world_state, agent, possible_actions):
  return state.find_possible_cells(world_state, agent, possible_actions)
    
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

if __name__ == "__main__" :
    main();