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