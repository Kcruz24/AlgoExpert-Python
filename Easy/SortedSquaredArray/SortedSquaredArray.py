# O(Nlog(N)) time | O(N) space
def sortedSquaredArray(array):
	output = []
	for num in array:
		num *= num
		output.append(num)
	return sorted(output)
	
	
# O(N) time | O(N) space
def sortedSquaredArray(array):
    sortedSquares = [0 for num in array]

    startIdx = 0
    endIdx = len(array) - 1
    
    lastSortedSquaredIdx = len(sortedSquares) - 1

    while startIdx <= endIdx:
        startVal = array[startIdx]
        endVal = array[endIdx]

        startSqrt = abs(startVal) ** 2
        endSqrt = endVal ** 2

        if startSqrt > endSqrt:
            sortedSquares[lastSortedSquaredIdx] = startSqrt
            startIdx += 1
        else:
            sortedSquares[lastSortedSquaredIdx] = endSqrt
            endIdx -= 1

        lastSortedSquaredIdx -= 1

    return sortedSquares


# Algo Expert
# O(N) time | O(N) space
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    smallest_val_idx = 0
    larger_val_idx = len(array) - 1

    for i in reversed(range(len(array))):
        smallest_val = array[smallest_val_idx] 
        larger_val = array[larger_val_idx]

        if abs(larger_val) > abs(smallest_val):
            sortedSquares[i] = larger_val ** 2
            larger_val_idx -= 1
        else:
            sortedSquares[i] = smallest_val ** 2
            smallest_val_idx += 1

    return sortedSquares


# Nov 30, 2021
# O(NLog(N)) time | O(1) space
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = abs(array[i] ** 2)
    return sorted(array)

array = [1, 2, 3, 5, 6, 8, 9]
array2 = [-5, -4, -3, -2, -1]


if __name__ == '__main__':

    print(sortedSquaredArray(array2))