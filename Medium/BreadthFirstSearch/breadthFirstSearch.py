class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(N) time | O(N) space
    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]

        while len(queue) > 0:
            node = queue.pop(0)

            array.append(node.name)

            for i in range(len(node.children)):
                queue.append(node.children[i])

        return array
