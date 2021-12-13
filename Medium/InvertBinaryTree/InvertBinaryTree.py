class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

# O(N) time | O(D) space
def invertBinaryTree(tree):
	return invertedBinaryTree(tree)

def invertedBinaryTree(tree):

	if tree is None:
		return

	leftTree = invertedBinaryTree(tree.left)
	rightTree = invertedBinaryTree(tree.right)

	tree.left, tree.right = tree.right, tree.left

	return tree