class Qtable:
  def __init__(self):
    self.table = {
      'normal': {
          'up': 5,
          'down': 12,
          'left': 3,
          'right': 8,
          'forward': 4,
          'backward': 7
      },
      'risky': {
          'up': 0,
          'down': 0,
          'left': 0,
          'right': 0,
          'forward': 0,
          'backward': 0
      },
      'pickup': {
          'up': 0,
          'down': 0,
          'left': 0,
          'right': 0,
          'forward': 0,
          'backward': 0
      },
      'dropoff': {
        'up': 0,
        'down': 0,
        'left': 0,
        'right': 0,
        'forward': 0,
        'backward': 0
      }
    }
    

    '''
    
    def update (self, states, moves):
        - go in states and moves and use formula to change
        - we will use the formula to update the find_q_vals
        self.table[state][direction] += formula
        

    action file

    state = "what"
    moves = [up, down, left]
    whatever.update(state, moves)
    whatever.

    '''

  def find_q_vals (self, position, moves):
    q_vals = {}
    for direction in moves:
      q_vals[direction] = self.table[position][direction]
    return q_vals

# def main():
#     qtable = Qtable()
#     moves = ["up", "down"]
#     dict = {}
#     dict = qtable.find_q_vals("normal", moves)
#     print(dict)

# if __name__ == "__main__" :
#     main();