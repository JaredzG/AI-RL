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
        {'type': 'normal', 'reward': -1, 'occupied_by': 'f'},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10},
        {'type': 'risky', 'reward': -2, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ]
    ]
    second_level = [
      [
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'risky', 'reward': -2, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'pickup', 'reward': +14, 'occupied_by': '', 'block_count': 10}
      ]
    ]
    third_level = [
      [
        {'type': 'dropoff', 'reward': +14, 'occupied_by': '', 'block_count': 0},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'dropoff', 'reward': +14, 'occupied_by': 'm', 'block_count': 0}
      ],
      [
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''},
        {'type': 'normal', 'reward': -1, 'occupied_by': ''}
      ]
    ]
    self.environment = [first_level, second_level, third_level]
    
  def move_agent(self, old_coords, action, agent):
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
    match self.environment[new_coords[0]][new_coords[1]][new_coords[2]]['type']:
      case 'pickup':
        self.remove_pickup_block(new_coords)
      case 'dropoff':
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
        cells[action] = environment[initial_position[0] + 1][initial_position[1]][initial_position[2]]['type']
      case 'down':
        cells[action] = environment[initial_position[0] - 1][initial_position[1]][initial_position[2]]['type']
      case 'backward':
        cells[action] = environment[initial_position[0]][initial_position[1] + 1][initial_position[2]]['type']
      case 'forward':
        cells[action] = environment[initial_position[0]][initial_position[1] - 1][initial_position[2]]['type']
      case 'right':
        cells[action] = environment[initial_position[0]][initial_position[1]][initial_position[2] + 1]['type']
      case 'left':
        cells[action] = environment[initial_position[0]][initial_position[1]][initial_position[2] - 1]['type']
  return cells

# def main():
#     env = Environment()
#     cells = get_cell_types(env, [0, 1, 1], ['up', 'left', 'right', 'forward', 'backward'])
#     print(cells)

# if __name__ == "__main__" :
#     main();