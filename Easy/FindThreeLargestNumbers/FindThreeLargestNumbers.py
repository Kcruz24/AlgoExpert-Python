# O(N) time | O(1) space
def findThreeLargestNumbers(array):
	largestNums = [array[0], array[1], array[2]]
	largestNums.sort()
	
	for idx, num in enumerate(array):
		if num > largestNums[0] and num not in largestNums:
			largestNums.pop(0)
			largestNums.insert(0, num)
		largestNums.sort()
			
	return largestNums