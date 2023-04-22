import environment

class State:
  def __init__(self, environment):
    self.environment = environment
    self.representation = {'male_position': [], 'female_position': [], 'male_carrying': False, 'female_carrying': False, 'pickup_cell_blocks': {}, 'dropoff_cell_blocks': {}}
    
  def set_male_position(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupied_by'] is 'm':
            self.representation['male_position'] = [x, y, z]
            
  def set_female_position(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['occupied_by'] is 'f':
            self.representation['female_position'] = [x, y, z]
            
  def toggle_male_carrying(self):
    self.representation['male_carrying'] = not self.representation['male_carrying']

  def toggle_female_carrying(self):
    self.representation['female_carrying'] = not self.representation['female_carrying']
    
  def set_pickup_cells_blocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] is 'pickup':
            self.representation[(x, y, z)] = self.environment[x][y][z]['block_count']
 
  def set_dropoff_cell_blocks(self):
    for x in range(3):
      for y in range(3):
        for z in range(3):
          if self.environment[x][y][z]['type'] is 'dropoff':
            self.representation[(x, y, z)] = self.environment[x][y][z]['block_count']
              
  