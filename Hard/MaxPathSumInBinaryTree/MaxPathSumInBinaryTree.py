class BinaryTree:
	def __init__(self, value, right=None, left=None):
		self.value = value
		self.right = right
		self.left = left

	def insert(self, values, i=0):
		if i >= len(values):
			return
		queue = [self]
		while len(queue) > 0:
			current = queue.pop(0)
			if current.left is None:
				current.left = BinaryTree(values[i])
				break
			queue.append(current.left)
			if current.right is None:
				current.right = BinaryTree(values[i])
				break
			queue.append(current.right)
		self.insert(values, i + 1)
		return self


# # Attempt before seing the code walkthrough
# def maxPathSum(tree):
# 	return max(calculateMaxPathSum(tree))

# def calculateMaxPathSum(node):
# 	nodeValue = node.value

# 	if node is None:
# 		return (nodeValue, nodeValue)

# 	leftBranchSum, leftTriangleSum = calculateMaxPathSum(node.left)
# 	rightBranchSum, rightTriangleSum = calculateMaxPathSum(node.right)
# 	maxChildBranch = max(rightBranchSum[0], leftBranchSum[0])

# 	maxPathSumBranch = max(maxChildBranch + nodeValue, nodeValue)
# 	maxPathSumTriangle = max(maxPathSumBranch, leftBranchSum[0] + nodeValue + rightBranchSum[0])
# 	runningMaxPathSum = max(leftBranchSum[0], rightBranchSum[0], maxPathSumTriangle)

# 	return (maxPathSumBranch, runningMaxPathSum)



# Attempt while seing the code walkthrough
def maxPathSum(tree):
	return max(findMaxSum(tree))

def findMaxSum(tree):

	if tree is None:
		return (0, float('-inf'))

	left_max_sum_branch, left_max_triangle_sum = findMaxSum(tree.left)
	right_max_sum_branch, right_max_triangle_sum = findMaxSum(tree.right)

	max_child_branch = max(right_max_sum_branch, left_max_sum_branch)

	max_path_sum_branch = max_child_branch + tree.value # 10
	calculate_triangle = left_max_sum_branch + tree.value + right_max_sum_branch # 16

	max_path_sum_triangle = max(max_path_sum_branch, calculate_triangle) # 10 vs 16
	running_max_path_sum = max(left_max_triangle_sum, right_max_triangle_sum, max_path_sum_triangle)

	print((max_path_sum_branch, running_max_path_sum))

	return (max_path_sum_branch, running_max_path_sum)



if __name__ == '__main__':
	test = BinaryTree(1).insert([2, 5, -4, -5, 6, 7])

	result = maxPathSum(test)
	print(result)
	result
	print('Result')

	print(result == 18)

