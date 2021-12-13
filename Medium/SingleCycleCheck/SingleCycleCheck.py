# O(N) time | O(1) space
def hasSingleCycle(array):
	num_elements_visited = 0
	cur_idx = 0

	while num_elements_visited < len(array):
		if num_elements_visited > 0 and cur_idx == 0:
			return False
		num_elements_visited += 1
		cur_idx = getNextIdx(cur_idx, array)

	return cur_idx == 0


def getNextIdx(cur_idx, array):
	return (array[cur_idx] + cur_idx) % len(array)


if __name__ == '__main__':
	array = [2, 3, 1, -4, -4, 2]

	print(hasSingleCycle(array))