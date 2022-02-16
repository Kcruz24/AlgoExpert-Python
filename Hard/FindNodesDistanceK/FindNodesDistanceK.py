# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# AlgoExpert Solution 1 - BFS
# O(N) time | O(N) space
def findNodesDistanceK(tree, target, k):
    nodes_to_parent = {}
    populate_nodes_to_parents(tree, nodes_to_parent)
    target_node = get_node_from_value(target, tree, nodes_to_parent)

    return bfs_for_nodes_distance_k(target_node, nodes_to_parent, k)


def bfs_for_nodes_distance_k(target_node, nodes_to_parent, k):
    queue = [(target_node, 0)]
    seen = {target_node.value}

    while len(queue) > 0:
        cur_node, distance_from_target = queue.pop(0)

        if distance_from_target == k:
            nodes_distance_k = [node.value for node, _ in queue]
            nodes_distance_k.append(cur_node.value)

            return nodes_distance_k

        parent_node = nodes_to_parent[cur_node.value]
        connected_nodes = [cur_node.left, cur_node.right, parent_node]
        for node in connected_nodes:
            if node is None or node.value in seen:
                continue

            seen.add(node.value)
            queue.append((node, distance_from_target + 1))

    return []


def get_node_from_value(target, tree, nodes_to_parent):
    if tree.value == target:
        return tree

    node_parent = nodes_to_parent[target]
    if node_parent.left and node_parent.left.value == target:
        return node_parent.left

    return node_parent.right


def populate_nodes_to_parents(node, nodes_to_parent, parent=None):
    if node is not None:
        nodes_to_parent[node.value] = parent
        populate_nodes_to_parents(node.left, nodes_to_parent, node)
        populate_nodes_to_parents(node.right, nodes_to_parent, node)



if __name__ == '__main__':
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)
    root.right.right.left = BinaryTree(7)
    root.right.right.right = BinaryTree(8)
    target = 3
    k = 2
    expected = [2, 7, 8]
    actual = findNodesDistanceK(root, target, k)
    actual.sort()
    print(actual == expected)





