'''

target - is an integer
input can be empty
the tree is a tradional tree, meaning that it has only two childs
will I get duplicate values?


                1
              /    \
             2       3
              \       \
               5       6
                      /  \
                     7    8


(2, 2)

[(8, 2), (7, 2)]
'''

# This is an input class. Do not edit.


from collections import deque


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(N) Time | O(N) Space


def findNodesDistanceK(tree, target, k):
    if tree is None:
        return []

    nodes_to_parent = {}
    populate_parents(tree, nodes_to_parent)

    target_node = get_target_object(tree, target, nodes_to_parent)

    return bfs_for_nodes_distance_k(target_node, nodes_to_parent, k)


def bfs_for_nodes_distance_k(target_node, nodes_to_parent, k):
    queue = deque([(target_node, 0)])
    seen = set([target_node.value])

    while queue:
        curr_node, distance = queue.popleft()

        if distance == k:
            nodes_distance_k = [node.value for node, _ in queue]
            nodes_distance_k.append(curr_node.value)

            return nodes_distance_k

        parent = nodes_to_parent[curr_node.value]
        neighbors = [curr_node.left, curr_node.right, parent]
        for neighbor in neighbors:
            if neighbor is not None and neighbor.value not in seen:
                queue.append((neighbor, distance + 1))
                seen.add(neighbor.value)

    return []


def populate_parents(node, nodes_to_parent, parent=None):
    if node is not None:
        nodes_to_parent[node.value] = parent
        populate_parents(node.left, nodes_to_parent, node)
        populate_parents(node.right, nodes_to_parent, node)


def get_target_object(tree, target, nodes_to_parent):
    if target == tree.value:
        return tree

    parent = nodes_to_parent[target]

    if parent.left and parent.left.value == target:
        return parent.left

    return parent.right
