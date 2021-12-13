class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(N) time | O(N) space
def findSuccessor(tree, node):
    allNodes = getNodes(tree, [])
    
    if node not in allNodes:
        return None
    
    nodeIdx = allNodes.index(node)
    
    if nodeIdx + 1 >= len(allNodes):
        return None
    
    successor = allNodes[nodeIdx + 1]
    return successor

def getNodes(tree, array):
    if tree is None:
        return array

    getNodes(tree.left, array)
    array.append(tree)
    getNodes(tree.right, array)

    return array



if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.left.parent = root
    root.right = BinaryTree(3)
    root.right.parent = root
    root.left.left = BinaryTree(4)
    root.left.left.parent = root.left
    root.left.right = BinaryTree(5)
    root.left.right.parent = root.left
    root.left.left.left = BinaryTree(6)
    root.left.left.left.parent = root.left.left
    node = root.left.right
    expected = root
    actual = findSuccessor(root, node)
    
    print(actual == expected)
