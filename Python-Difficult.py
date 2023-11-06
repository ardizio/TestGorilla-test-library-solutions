def max_treasure(treasure_map):
  # Handle the edge case where the treasure map is empty or has no columns
  if not treasure_map or not treasure_map[0]:
      return 0

  def dfs(row, col, value):
      # Mark the current cell as seen
      seen.add((row, col))
      # Update the maximum value for the current cell
      dp[row][col] = max(dp[row][col], value)
      # Define the relative coordinates of neighboring cells (up, down, left, right)
      neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
      # Loop through each neighboring cell
      for neighbor_row, neighbor_col in neighbors:
          # Check if the neighbor cell is within the boundaries of the treasure map
          if 0 <= neighbor_row < x and 0 <= neighbor_col < y:
              # Check if the neighbor cell has treasure and has not been visited yet
              if treasure_map[neighbor_row][neighbor_col] and (neighbor_row, neighbor_col) not in seen:
                  # Recursively explore the neighbor cell and update the value
                  new_value = value + treasure_map[neighbor_row][neighbor_col]
                  dfs(neighbor_row, neighbor_col, new_value)
      # Remove the current cell from the seen set when done
      seen.discard((row, col))


  # Get the dimensions of the treasure map
  x = len(treasure_map)
  y = len(treasure_map[0])

  # Initialize a xD array to store the maximum values
  dp = [[0] * y for _ in range(x)]

  for i in range(x):
      for j in range(y):
          # Check if a cell has a negative value, which is not allowed
          if treasure_map[i][j] < 0:
              return -1
          # Check if the cell has a positive value (treasure)
          if treasure_map[i][j]:
              # Initialize a set to keep track of seen cells for each exploration
              seen = set()
              dfs(i, j, treasure_map[i][j])

  # Find the maximum treasure value in the dp array
  max_treasure = max(c for row in dp for c in row)
  return max_treasure


ini = [[3, 0, 0, 1, 2],[0,1,4,0,0],[5,0,0,3,3]]
sec = [[3, 0, 0, 1, 2],[0,1,4,0,0],[5,0,0,3,0]]

print(max_treasure(ini))
print(max_treasure(sec))
