# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Not optimal
# O(N^2) Time | O(N) Space
def reconstructBst(values):
    if len(values) == 0:
        return

    root = values[0]
    right_subtree_idx = len(values)

    for i in range(1, len(values)):
        if values[i] >= root:
            right_subtree_idx = i
            break

    left_subtree = values[1:right_subtree_idx]
    right_subtree = values[right_subtree_idx:]
    left = reconstructBst(left_subtree)
    right = reconstructBst(right_subtree)

    return BST(root, left, right)
