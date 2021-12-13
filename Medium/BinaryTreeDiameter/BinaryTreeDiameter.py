class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# (N) time | O(H) space
def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter


def getTreeInfo(node):
    if node is None:
        return TreeInfo(0, 0)

    left_tree_info = getTreeInfo(node.left)
    right_tree_info = getTreeInfo(node.right)

    longest_path_through_current_node = right_tree_info.height + left_tree_info.height
    current_max_diameter = max(right_tree_info.diameter,left_tree_info.diameter)
    current_diameter = max(longest_path_through_current_node, current_max_diameter)
    current_height = 1 + max(right_tree_info.height, left_tree_info.height)
                        
    return TreeInfo(current_height, current_diameter)


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.left.left = BinaryTree(7)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.right = BinaryTree(4)
    root.left.right.right = BinaryTree(5)
    root.left.right.right.right = BinaryTree(6)
    root.right = BinaryTree(2)
    expected = 6
    actual = binaryTreeDiameter(root)


    print('Diameter', binaryTreeDiameter(root))
    print(actual == expected)
