# Algo Expert optimal solution
# O(wh) time | O(wh) space
def removeIslands(matrix):
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			row_is_border = row == 0 or row == len(matrix) - 1
			col_is_border = col == 0 or col == len(matrix[row]) - 1

			is_border = row_is_border or col_is_border

			if not is_border:
				continue

			if matrix[row][col] != 1:
				continue

			change_ones_connected_to_border_to_twos(matrix, row, col)

	for row in range(len(matrix)):
		for col in range(len(matrix[row])):

			color = matrix[row][col]
			if color == 1:
				matrix[row][col] = 0
			elif color == 2:
				matrix[row][col] = 1

	return matrix

# Depth-first search
def change_ones_connected_to_border_to_twos(matrix, start_row, start_col):
	stack = [(start_row, start_col)]

	while len(stack) > 0:
		current_position = stack.pop()
		current_row, current_col = current_position

		matrix[current_row][current_col] = 2

		neighbors = get_neigbhors(matrix, current_row, current_col)
		for neighbor in neighbors:
			row, col = neighbor

			if matrix[row][col] != 1:
				continue

			stack.append(neighbor)

def get_neigbhors(matrix, row, col):
	neighbors = []

	num_rows = len(matrix)
	num_cols = len(matrix[row])

	if row - 1 >= 0: #UP
		neighbors.append((row - 1, col))
	if row + 1 < num_rows: # DOWN
		neighbors.append((row + 1, col))
	if col - 1 >= 0: # LEFT
		neighbors.append((row, col - 1))
	if col + 1 < num_cols:
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

















