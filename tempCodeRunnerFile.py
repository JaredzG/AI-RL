  actions = set_possible_actions(world_state, agent.type)
    print('actions ', actions)
    cells = set_possible_cells(world_state, agent.type, actions)
    print('cells ', cells)
    q_vals = set_possible_action_q_vals(world_state, agent.type, q_table, actions)
    print('q_vals ', q_vals)
    chosen_action = choose_action(agent, cells, q_vals, chosen_policy)
    print('chosen_action ', chosen_action)
    next_pos_actions = set_next_position_possible_actions(world_state, agent.type, chosen_action)
    print('next_pos_actions ', next_pos_actions)
    next_pos_cells = set_next_position_possible_cells(world_state, cells[chosen_action]['coords'], next_pos_actions)
    print('next_pos_cells ', next_pos_cells)
    future_carrying = False
    if (rl_method == 'sarsa'):
      future_carrying = determine_future_carrying(agent, cells, chosen_action)
    q_table.update_qtable(world_state.representation['male_position']['cell_type'], chosen_action, cells[chosen_action]['type'], next_pos_actions, 0.2, 0.6, rl_method, chosen_policy, future_carrying, next_pos_cells)
    print(q_table.table)
    if cells[chosen_action]['type'] == 'pickup' or cells[chosen_action]['type'] == 'dropoff':
      pickup_or_dropoff(agent, cells[chosen_action]['type'])
    print('agent carrying', agent.carrying)
    if agent.type == 'm':
      world_state.update_environment_and_state(world_state.representation['male_position']['coords'], chosen_action, agent.type, agent.carrying, cells[chosen_action]['type'])
    else:
      world_state.update_environment_and_state(world_state.representation['female_position']['coords'], chosen_action, agent.type, agent.carrying, cells[chosen_action]['type'])
    print('new environment:')
    for x in range(3):
      print(f'\nLevel {x}\n')
      for y in range(3):
        print(f'Row {y}\n')
        for z in range(3):
          print(world_state.environment[x][y][z])