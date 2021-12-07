class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur_node = self
        while cur_node is not None:
            if value > cur_node.value:
                if cur_node.right is not None:
                    cur_node = cur_node.right
                else:
                    cur_node.right = BST(value)

            elif value < cur_node.value:
                if cur_node.left is not None:
                    cur_node = cur_node.left
                else:
                    cur_node.left = BST(value)
            else:
                break

        return self

    # Average: O(log(N)) time | O(1) space
    # Worst: O(N) time | O(1) space
    def contains(self, value):
        # Write your code here.
        cur_node = self
        while cur_node is not None:
            if value > cur_node.value:
                cur_node = cur_node.right
            elif value < cur_node.value:
                cur_node = cur_node.left
            else:
                return True
        return False

    def remove(self, value, parent_node=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur_node = self
        while cur_node is not None:

            if value < cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.left

            elif value > cur_node.value:
                parent_node = cur_node
                cur_node = cur_node.right

            else:
                if cur_node.left is not None and cur_node.right is not None:
                    cur_node.value = cur_node.right.getMostLeftNode()
                    cur_node.right.remove(cur_node.value, cur_node)

                elif parent_node is None:
                    if cur_node.left is not None:
                        cur_node.value = cur_node.right.value
                        cur_node.right = cur_node.left.right
                        cur_node.left = cur_node.left.left

                    elif cur_node.right is not None:
                        cur_node.value = cur_node.left.value
                        cur_node.left = cur_node.right.left
                        cur_node.right = cur_node.right.right
 
                    else:
                        # Single-node tree; do nothing.
                        pass

                elif parent_node.left == cur_node:
                    parent_node.left = cur_node.left if cur_node.left is not None else cur_node.right

                elif parent_node.right == cur_node:
                    parent_node.right = cur_node.left if cur_node.left is not None else cur_node.right
                break

        return self

    def getMostLeftNode(self):
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value


root = BST(10)
root.left = BST(7)
root.left.left = BST(5)
root.left.left.left = BST(1)
root.left.right = BST(8)
root.right = BST(20)
root.right.left = BST(11)
root.right.right = BST(25)
root.right.right.left = BST(22)

if __name__ == '__main__':
    root.insert(12)
    print(root.right.left.right.value == 12)

    print(root.contains(7))

    root.remove(7)

    print(root.contains(7))
