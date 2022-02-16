# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(N) time | O(H) space
def heightBalancedBinaryTree(tree):
    return isBinaryTreeBalanced(tree, True).isBalanced

def isBinaryTreeBalanced(tree, isBalanced):
    if tree is None:
        return TreeInfo(0, isBalanced)

    left_tree = isBinaryTreeBalanced(tree.left, isBalanced)
    right_tree = isBinaryTreeBalanced(tree.right, isBalanced)

    calculate_balance = abs(left_tree.height - right_tree.height) <= 1

    isBalanced = left_tree.isBalanced and right_tree.isBalanced and calculate_balance
    height = max(left_tree.height, right_tree.height) + 1

    return TreeInfo(height, isBalanced)


class TreeInfo:
    def __init__(self, height, isBalanced):
        self.height = height
        self.isBalanced = isBalanced


