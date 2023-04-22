import environment

class State:
  def __init__(self, environment):
    self.environment = environment
    self.representation = {'male_position': [], 'female_position': [], 'male_carrying': False, 'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}
    self.set_male_position()
    self.set_female_position()
    self.set_pickup_cells_blocks()
    self.set_dropoff_cell_blocks()
    
  def set_male_position(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupied_by'] == 'm':
            self.representation['male_position'] = [x, y, z]
            
  def set_female_position(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupied_by'] == 'f':
            self.representation['female_position'] = [x, y, z]
            
  def toggle_male_carrying(self):
    self.representation['male_carrying'] = not self.representation['male_carrying']

  def toggle_female_carrying(self):
    self.representation['female_carrying'] = not self.representation['female_carrying']
    
  def set_pickup_cells_blocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] == 'pickup':
            self.representation['pickup_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']
 
  def set_dropoff_cell_blocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] == 'dropoff':
            self.representation['dropoff_cell_blocks'][(x, y, z)] = self.environment[x][y][z]['block_count']
              
def find_possible_cells(state, agent, actions):
  possible_cells = {}
  if agent == 'm':
    possible_cells = environment.get_cell_types(state.environment, state.representation['male_position'], actions)
  else:
    possible_cells = environment.get_cell_types(state.environment, state.representation['female_position'], actions)
  return possible_cells

# def main():
#     env = environment.Environment()
#     state = State(env.environment)
#     cells = find_possible_cells(state, 'm', ['down', 'left', 'forward', 'backward'])
#     print(cells)

# if __name__ == "__main__" :
#     main();