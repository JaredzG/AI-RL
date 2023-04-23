  print('new environment:')
  for x in range(3):
    print(f'Level {x}\n')
    for y in range(3):
      print(f'Row {y}\n')
      for z in range(3):
        print(f'Column {z}\n')
        print(world_state.environment[x][y][z], '\n')