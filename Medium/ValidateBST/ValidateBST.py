# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# (N) time | O(D) space 
def validateBst(tree):
    # Write your code here.
    return isValidBst(tree, float('-inf'), float('inf'))


def isValidBst(tree, minValue, maxValue):
    if tree is None:
        return True

    if minValue > tree.value or tree.value >= maxValue:
        return False

    leftIsValid = isValidBst(tree.left, minValue, tree.value)
    rightIsValid = isValidBst(tree.right, tree.value, maxValue)

    return leftIsValid and rightIsValid


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
    expected = True
    print(validateBst(root) == expected)
