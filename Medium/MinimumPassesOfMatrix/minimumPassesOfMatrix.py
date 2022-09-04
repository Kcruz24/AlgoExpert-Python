from collections import deque

# Two Queues
# O(W*H) Time | O(W*H) Space
def minimumPassesOfMatrix(matrix):
    passes = convert_negatives(matrix)

    return passes if not contains_negative(matrix) else -1


def convert_negatives(matrix):
    next_pass_queue = deque(get_all_positive_positions(matrix))

    passes = -1

    while len(next_pass_queue) > 0:
        curr_pass_queue = deque(next_pass_queue)
        next_pass_queue = []

        while len(curr_pass_queue) > 0:
            curr_row, curr_col = curr_pass_queue.popleft()

            neighbors = get_neighbors(curr_row, curr_col, matrix)

            for row, col in neighbors:
                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] *= -1
                    next_pass_queue.append([row, col])

        passes += 1

    return passes


def get_all_positive_positions(matrix):
    positive_positions = []

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] > 0:
                positive_positions.append([row, col])

    return positive_positions


def contains_negative(matrix):
    for row in matrix:
        for value in row:
            if value < 0:
                return True

    return False


def get_neighbors(row, col, matrix):
    stack = []

    row_length = len(matrix)
    col_length = len(matrix[0])

    if row - 1 >= 0:  # UP
        stack.append([row - 1, col])
    if row + 1 < row_length:
        stack.append([row + 1, col])
    if col - 1 >= 0:
        stack.append([row, col - 1])
    if col + 1 < col_length:
        stack.append([row, col + 1])

    return stack
