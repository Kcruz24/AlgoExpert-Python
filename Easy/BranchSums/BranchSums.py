# This is the class of the input root. Do not edit it.
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

    def inorder_traversal(self, root):
        order = []

        if root:
            order = self.inorder_traversal(root.left)
            order.append(root.value)
            order += self.inorder_traversal(root.right)

        return order


# Algo Expert Solution
# O(N) time | O(N) space
def branchSums(root):
    sums = []
    calculate_branch_sums(root, 0, sums)

    return sums


def calculate_branch_sums(node, running_sum, sums):
    if node is None:
        return

    new_running_sum = running_sum + node.value
    if node.right is None and node.left is None:
        sums.append(new_running_sum)
        return

    calculate_branch_sums(node.left, new_running_sum, sums)
    calculate_branch_sums(node.right, new_running_sum, sums)


tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])

if __name__ == "__main__":
    print(branchSums(tree))
    print(tree.inorder_traversal(tree))
