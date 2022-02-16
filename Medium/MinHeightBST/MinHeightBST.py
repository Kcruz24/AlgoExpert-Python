

# AlgoExpert Solution 3
# O(N) time | O(N) space
def minHeightBst(array):
    return constructMinHeightBst(array, 0, len(array) - 1)


def constructMinHeightBst(array, start_idx, end_idx):
    if end_idx < start_idx:
        return None

    mid_idx = (start_idx + end_idx) // 2
    bst = BST(array[mid_idx])
    bst.left = constructMinHeightBst(array, start_idx, mid_idx - 1)
    bst.right = constructMinHeightBst(array, mid_idx + 1, end_idx)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    return leftIsValid and validateBstHelper(tree.right, tree.value, maxValue)


def getTreeHeight(tree, height=0):
    if tree is None:
        return height
    leftTreeHeight = getTreeHeight(tree.left, height + 1)
    rightTreeHeight = getTreeHeight(tree.right, height + 1)
    return max(leftTreeHeight, rightTreeHeight)


if __name__ == '__main__':
    array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    tree = minHeightBst(array)

    print(validateBst(tree))
    print('Height', getTreeHeight(tree))
    print(getTreeHeight(tree) == 4)

    inOrder = inOrderTraverse(tree, [])

    print(inOrder == [1, 2, 5, 7, 10, 13, 14, 15, 22])
