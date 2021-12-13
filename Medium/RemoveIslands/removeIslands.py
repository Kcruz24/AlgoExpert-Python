
# O(wh) time | O(wh) space
def removeIslands(matrix):
    last_row = len(matrix) - 1
    last_col = len(matrix[0]) - 1

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_is_border = row == 0 or row == last_row
            col_is_border = col == 0 or col == last_col

            is_border = row_is_border or col_is_border

            if not is_border or matrix[row][col] != 1:
                continue

            change_ones_to_twos(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] > 0:
                matrix[row][col] -= 1
            
    return matrix

def change_ones_to_twos(matrix, row, col):
    stack = [(row, col)]

    while len(stack) > 0:
        current_row, current_col = stack.pop()
        
        neighbors = get_neigbhors(matrix, current_row, current_col)
        for row, col in neighbors:
            if matrix[row][col] == 1:
                stack.append((row, col))
            
        matrix[current_row][current_col] = 2

        
        
def get_neigbhors(matrix, row, col):
    neighbors = []

    row_length = len(matrix)
    col_length = len(matrix[row])


    if row - 1 >= 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < row_length:
        neighbors.append((row + 1, col))
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    if col + 1 < col_length:
        neighbors.append((row, col + 1))

    return neighbors


if __name__ == '__main__':
    sample_input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    expected = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    actual = removeIslands(sample_input)
    print(actual == expected)
