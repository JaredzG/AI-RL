# Environment module
# Cells have these features:
'''
{'type': 'normal', 'reward': -1, 'occupied_by': ''}
{'type': 'risky', 'reward': -2, 'occupied_by': ''}
{'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10}
{'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0}
'''

'''
Environment is sent to state, which is sent to agent. Agent makes move, changing the environment. Like a triangle cycle.
'''
class Environment:
  def __init__(self):
    first_level = [
      [
        {'type': 'normal', 'occupied_by': 'f'},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'dropoff', 'occupied_by': '', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'pickup', 'occupied_by': '', 'block_count': 10},
        {'type': 'risky', 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''}
      ]
    ]
    second_level = [
      [
        {'type': 'dropoff', 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'risky', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'pickup', 'occupied_by': '', 'block_count': 10}
      ]
    ]
    third_level = [
      [
        {'type': 'dropoff', 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'dropoff', 'occupied_by': '', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': ''},
        {'type': 'normal', 'occupied_by': 'm'}
      ]
    ]
    self.environment = [first_level, second_level, third_level]
    
  def move_agent(self, old_coords, action, agent, carrying):
    self.environment[old_coords[0]][old_coords[1]][old_coords[2]]['occupied_by'] = ''
    new_coords = []
    match action:
      case 'up':
        self.environment[old_coords[0] + 1][old_coords[1]][old_coords[2]]['occupied_by'] = agent
        new_coords = [old_coords[0] + 1, old_coords[1], old_coords[2]]
      case 'down':
        self.environment[old_coords[0] - 1][old_coords[1]][old_coords[2]]['occupied_by'] = agent
        new_coords = [old_coords[0] - 1, old_coords[1], old_coords[2]]
      case 'forward':
        self.environment[old_coords[0]][old_coords[1] + 1][old_coords[2]]['occupied_by'] = agent
        new_coords = [old_coords[0], old_coords[1] + 1, old_coords[2]]
      case 'backward':
        self.environment[old_coords[0]][old_coords[1] - 1][old_coords[2]]['occupied_by'] = agent
        new_coords = [old_coords[0], old_coords[1] - 1, old_coords[2]]
      case 'right':
        self.environment[old_coords[0]][old_coords[1]][old_coords[2] + 1]['occupied_by'] = agent
        new_coords = [old_coords[0], old_coords[1], old_coords[2] + 1]
      case 'left':
        self.environment[old_coords[0]][old_coords[1]][old_coords[2] - 1]['occupied_by'] = agent
        new_coords = [old_coords[0], old_coords[1], old_coords[2] - 1]
    print('new_cell_type ', self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['type'])
    print('carrying ', carrying)
    match self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['type']:
      case 'pickup':
        if carrying:
          self.remove_pickup_block(new_coords)
      case 'dropoff':
        if carrying == False:
          self.add_dropoff_block(new_coords)
      case 'normal':
        pass
      case 'risky':
        pass
        
  def remove_pickup_block(self, coords):
    if(self.environment[coords[0]][coords[1]][coords[2]]['block_count'] > 0):
      self.environment[coords[0]][coords[1]][coords[2]]['block_count'] -= 1
      
  def add_dropoff_block(self, coords):
    if(self.environment[coords[0]][coords[1]][coords[2]]['block_count'] < 5):
      self.environment[coords[0]][coords[1]][coords[2]]['block_count'] += 1
      
def get_cell_types(environment, initial_position, actions):
  cells = {}
  for action in actions:
    match action:
      case 'up':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0] + 1][initial_position[1]][initial_position[2]]['type']
        cells[action]['coords'] = [initial_position[0] + 1, initial_position[1], initial_position[2]]
      case 'down':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0] - 1][initial_position[1]][initial_position[2]]['type']
        cells[action]['coords'] = [initial_position[0] - 1, initial_position[1], initial_position[2]]
      case 'backward':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0]][initial_position[1] + 1][initial_position[2]]['type']
        cells[action]['coords'] = [initial_position[0], initial_position[1] + 1, initial_position[2]]
      case 'forward':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0]][initial_position[1] - 1][initial_position[2]]['type']
        cells[action]['coords'] = [initial_position[0], initial_position[1] - 1, initial_position[2]]
      case 'right':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] + 1]['type']
        cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] + 1]
      case 'left':
        cells[action] = {}
        cells[action]['type'] = environment[initial_position[0]][initial_position[1]][initial_position[2] - 1]['type']
        cells[action]['coords'] = [initial_position[0], initial_position[1], initial_position[2] - 1]
    coords = cells[action]['coords']
    if cells[action]['type'] == 'pickup':
      if environment[coords[0]][coords[1]][coords[2]]['block_count'] > 0:
        cells[action]['is_empty'] = False
      else:
        cells[action]['is_empty'] = True
    elif cells[action]['type'] == 'dropoff':
      if environment[coords[0]][coords[1]][coords[2]]['block_count'] < 5:
        cells[action]['is_full'] = False
      else:
        cells[action]['is_full'] = True
  return cells

# def main():
#     env = Environment()
#     cells = get_cell_types(env, [0, 1, 1], ['up', 'left', 'right', 'forward', 'backward'])
#     print(cells)

# if __name__ == "__main__" :
#     main();