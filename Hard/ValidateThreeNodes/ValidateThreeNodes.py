# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(D) time | O(1) space - Where "D" is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    isNodeOneAncestor = isAncestor(
        nodeOne, nodeTwo) and isAncestor(nodeTwo, nodeThree)
    isNodeThreeAncestor = isAncestor(
        nodeThree, nodeTwo) and isAncestor(nodeTwo, nodeOne)

    return isNodeOneAncestor or isNodeThreeAncestor

def isAncestor(ancestor, descendant):
    while ancestor:
        if descendant.value < ancestor.value:
            ancestor = ancestor.left
        elif descendant.value > ancestor.value:
            ancestor = ancestor.right
        else:
            return True

    return False


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