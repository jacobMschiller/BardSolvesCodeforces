def move_load(warehouse, loader_position, load_position, target_position):
  """Moves the load to the target position in the warehouse.

  Args:
    warehouse: A 2D list of characters representing the warehouse.
    loader_position: The current position of the loader.
    load_position: The current position of the load.
    target_position: The target position of the load.

  Returns:
    A string representing the sequence of moves and pushes that the loader needs to make to move the load to the target position.
  """

  moves = []
  while loader_position != target_position:
    # Move the loader to the adjacent cell containing the load.
    moves.append(get_move(loader_position, load_position))

    # Push the load to the target position.
    moves.append(get_push(loader_position, target_position))

  return "YES\n" + "".join(moves)


def get_move(source_position, target_position):
  """Returns the direction in which the loader needs to move to reach the target position.

  Args:
    source_position: The current position of the loader.
    target_position: The target position of the loader.

  Returns:
    A character representing the direction of the move.
  """

  if source_position[0] < target_position[0]:
    return "N"
  elif source_position[0] > target_position[0]:
    return "S"
  elif source_position[1] < target_position[1]:
    return "W"
  else:
    return "E"


def get_push(source_position, target_position):
  """Returns the direction in which the loader needs to push the load to reach the target position.

  Args:
    source_position: The current position of the loader.
    target_position: The target position of the load.

  Returns:
    A character representing the direction of the push.
  """

  if source_position[0] < target_position[0]:
    return "S"
  elif source_position[0] > target_position[0]:
    return "N"
  elif source_position[1] < target_position[1]:
    return "E"
  else:
    return "W"


if __name__ == "__main__":
  # Read the input.
  n, m = [int(x) for x in input().split()]
  warehouse = []
  for i in range(n):
    warehouse.append(list(input()))

  # Find the positions of the loader and the load.
  loader_position = None
  load_position = None
  for i in range(n):
    for j in range(m):
      if warehouse[i][j] == "Y":
        loader_position = (i, j)
      elif warehouse[i][j] == "B":
        load_position = (i, j)

  # Find the target position of the load.
  target_position = None
  for i in range(n):
    for j in range(m):
      if warehouse[i][j] == "T":
        target_position = (i, j)

  # Move the load to the target position.
  moves = move_load(warehouse, loader_position, load_position, target_position)

  # Print the output.
  if moves == "NO":
    print("NO")
  else:
    print(moves)
