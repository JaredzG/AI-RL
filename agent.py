import action
import qtable
import state
import environment
class Agent:
  def __init__(self, type, state, carrying = False):
    self.type = type
    self.state = state
    self.carrying = carrying
    
  def toggle_carrying(self):
    self.carrying = not self.carrying
    
  def set_possible_actions(self):
    self.possible_actions = action.find_possible_actions(self.state, self.type)
    
  def set_possible_cells(self):
    self.possible_cells = state.find_possible_cells(self.state, self.type, self.possible_actions)
    
def main():
    env = environment.Environment()
    cur_state = state.State(env.environment)
    agent = Agent('m', cur_state)
    agent.set_possible_actions()
    actions = agent.possible_actions
    print("action ", actions)
    agent.set_possible_cells()
    cells = agent.possible_cells
    print("cells", cells)

if __name__ == "__main__" :
    main();