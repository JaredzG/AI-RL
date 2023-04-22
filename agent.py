import action
class Agent:
  def __init__(self, type, actions, carrying):
    self.type = type
    self.actions = actions
    self.carrying = carrying
    
  def set_actions(self, new_actions):
    self.actions = new_actions
    
  def toggle_carrying(self):
    self.carrying = not self.carrying
    