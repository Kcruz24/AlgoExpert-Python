# O(N^2) time | O(1) space
def selectionSort(array):
	for i in range(len(array)):
		smallestNum = float('inf')
		smallestNumIdx = 0
		for j in range(i + 1, len(array)):
			if array[j] < smallestNum:
				smallestNum = array[j]
				smallestNumIdx = j

		if array[i] > smallestNum:
			swap(i, smallestNumIdx, array)

	return array


# O(N^2) time | O(1) space - (2nd Solution)
def selectionSort(array):
    for i in range(len(array)):
        lowest = array[i]
        lowestIdx = i
        for j in range(i + 1, len(array)):
            if array[j] < lowest:
                lowest = array[j]
                lowestIdx = j
        swap(i, lowestIdx, array)

    return array


def swap(idx_one, idx_two, array):
    array[idx_one], array[idx_two] = array[idx_two], array[idx_one]

