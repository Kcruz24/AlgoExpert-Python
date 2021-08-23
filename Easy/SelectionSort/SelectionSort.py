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