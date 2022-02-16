# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# AlgoExpert Solution 2
# O(H) time | O(1) space
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    if isAncestor(nodeOne, nodeTwo):
        return isAncestor(nodeTwo, nodeThree)

    if isAncestor(nodeThree, nodeTwo):
        return isAncestor(nodeTwo, nodeOne)

    return False


def isAncestor(ancestorNode, targetNode):
    while ancestorNode is not None and ancestorNode is not targetNode:
        ancestorNode = ancestorNode.left if targetNode.value > ancestorNode.value else ancestorNode.right

    return ancestorNode is targetNode


if __name__ == '__main__':
    root = BST(5)
    root.left = BST(2)
    root.right = BST(7)
    root.left.left = BST(1)
    root.left.right = BST(4)
    root.right.left = BST(6)
    root.right.right = BST(8)
    root.left.left.left = BST(0)
    root.left.right.left = BST(3)

    nodeOne = root
    nodeTwo = root.left
    nodeThree = root.left.right.left
    expected = True
    actual = validateThreeNodes(nodeOne, nodeTwo, nodeThree)
    print(actual == expected)