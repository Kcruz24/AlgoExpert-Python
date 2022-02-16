def riverSizes(matrix):
    # Write your code here.
    visited_nodes = [[False for col in matrix[0]] for row in matrix]
    river_sizes = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if matrix[row][col] == 1 and not visited_nodes[row][col]:
                current_river_size = calculate_river_size(matrix, visited_nodes,
                                                          row, col)
                river_sizes.append(current_river_size)

    return river_sizes


def calculate_river_size(matrix, visited_nodes, row, col):
    stack = [(row, col)]
    running_sum = 0

    while len(stack) > 0:
        row, col = stack.pop()

        if visited_nodes[row][col]:
            continue

        visited_nodes[row][col] = True

        neighbors = get_neighbors(matrix, row, col)

        for row, col in neighbors:
            if matrix[row][col] == 1:
                stack.append((row, col))

        running_sum += 1

    return running_sum


def get_neighbors(matrix, row, col):
    neighbors = []

    row_length = len(matrix)
    col_lenght = len(matrix[row])

    if row - 1 >= 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < row_length:  # DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < col_lenght:
        neighbors.append((row, col + 1))

    return neighbors


if __name__ == "__main__":
    rivers = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]

    print(riverSizes(rivers))
