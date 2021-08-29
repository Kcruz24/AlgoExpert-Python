# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


# Algo Expert iterative approach
# O(N) time | O(H) space - where N is the number of nodes and H is the height
# of the tree.
def nodeDepthsIterative(root):
    sum_of_depths = 0
    stack = [{"node": root, "depth": 0}]

    while len(stack) > 0:
        node_info = stack.pop()
        node = node_info["node"]
        depth = node_info["depth"]

        if node is None:
            continue

        sum_of_depths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})

    return sum_of_depths


# Algo Expert recursive approach
# O(N) time | O(H) space - where N is the number of nodes and H is the height
# of the tree.
def nodeDepths(root, depth=0):
    if root is None:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == '__main__':
    print(nodeDepths(tree))
