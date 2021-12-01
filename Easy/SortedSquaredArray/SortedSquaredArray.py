# O(Nlog(N)) time | O(N) space
def sortedSquaredArray(array):
	output = []
	for num in array:
		num *= num
		output.append(num)
	return sorted(output)
	
	
# O(N) time | O(N) space
def sortedSquaredArray2(array):
	output = [0 for _ in array]
	
	start = 0
	end = len(array) - 1
	idx = len(output) - 1
	
	while start < end:
		startVal = array[start]
		endVal = array[end]
		
		if abs(startVal) > abs(endVal):
			output[idx] = pow(startVal, 2)
			start += 1
		elif abs(endVal) > abs(startVal):
			output[idx] = pow(endVal, 2)
			end -= 1
		
		idx -= 1
		
	output[idx] = pow(array[start], 2)
	return output


# Nov 30, 2021
# O(N) time | O(1) space
def sortedSquaredArray(array):
    for i in range(len(array)):
        array[i] = abs(array[i] ** 2)
    return sorted(array)

array = [1, 2, 3, 5, 6, 8, 9]
array2 = [-5, -4, -3, -2, -1]


if __name__ == '__main__':

    print(sortedSquaredArray(array2))