# AlgoExpert Solution
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


# My Solution
# O(N) time | O(N) space
def hasSingleCycle2(array):
    curr_idx = getNextIdx(0, array)
    visited_idx = []

    for _ in range(len(array)):
        if curr_idx not in visited_idx:
            visited_idx.append(curr_idx)
            curr_idx = getNextIdx(curr_idx, array)

            if curr_idx in visited_idx:
                return False

            if curr_idx not in visited_idx and len(visited_idx) == len(array) - 1:
                return True

    return False


def getNextIdx(cur_idx, array):
	return (array[cur_idx] + cur_idx) % len(array)


if __name__ == '__main__':
	array = [2, 3, 1, -4, -4, 2]

	print(hasSingleCycle2(array))