# Recursive approach
# Avg: O(log(N)) time | O(log(N)) space
# Worst: O(N) time | O(N) space
def findClosestValueInBst(tree, target):
	return findClosestHelper(tree, target, float('inf'))
		
	
def findClosestHelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	
	if target < tree.value:
		return findClosestHelper(tree.left, target, closest)
	elif target > tree.value:
		return findClosestHelper(tree.right, target, closest)
	else:
		return closest
		
		
# Iterative approach
# Avg: O(log(N)) time | O(1) space
# Worst: O(N) time | O(1) space
def findClosestValueInBstIterative(tree, target):
	closest = float('inf')
	currentNode = tree
	
	while currentNode is not None:
		if abs(target - closest) > abs(target - currentNode.value):
			closest = currentNode.value
		
		if target < currentNode.value:
			currentNode = currentNode.left
		elif target > currentNode.value:
			currentNode = currentNode.right
		else:
			break
			
	return closest
	

# This is the class of the input tree. Do not edit.
class BST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		
		
if __name__ == '__main__':
	root = BST(10)
	root.left = BST(5)
	root.left.left = BST(2)
	root.left.left.left = BST(1)
	root.left.right = BST(5)
	root.right = BST(15)
	root.right.left = BST(13)
	root.right.left.right = BST(14)
	root.right.right = BST(22)
	
	expected = 13
	print(findClosestValueInBst(root, 12))
	print(findClosestValueInBstIterative(root, 12) == expected)