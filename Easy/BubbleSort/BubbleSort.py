# O(N^2) time | O(1) space
def bubbleSort(array):
	for i in range(len(array)):
		for j in range(i + 1, len(array)):
			if array[i] > array[j]:
				swap(i, j, array)
	
	return array
	
	
def swap(idx1, idx2, arr):
	arr[idx1], arr[idx2] = arr[idx2], arr[idx1]