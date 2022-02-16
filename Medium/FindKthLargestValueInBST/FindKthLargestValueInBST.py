# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    values = []
    get_nodes_values(tree, values)

    kth_position = -1 * k

    return values[kth_position]


def get_nodes_values(tree, values):
    if tree is None:
        return

    get_nodes_values(tree.left, values)
    values.append(tree.value)
    get_nodes_values(tree.right, values)


if __name__ == '__main__':
    root = BST(15)
    root.left = BST(5)
    root.left.left = BST(2)
    root.left.left.left = BST(1)
    root.left.left.right = BST(3)
    root.left.right = BST(5)
    root.right = BST(20)
    root.right.left = BST(17)
    root.right.right = BST(22)
    k = 3
    expected = 17
    actual = findKthLargestValueInBst(root, k)
    print(actual == expected)
