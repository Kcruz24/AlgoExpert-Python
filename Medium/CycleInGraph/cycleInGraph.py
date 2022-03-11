# AlgoExpert Solution 1
# O(V + E) time | O(V) space
class Solution1:
    def cycleInGraph(self, edges):
        numberOfNodes = len(edges)
        visited = [False for _ in range(numberOfNodes)]
        inStack = [False for _ in range(numberOfNodes)]

        for node in range(numberOfNodes):
            if visited[node]:
                continue

            containsCycle = self.isNodeInCycle(edges, node, visited, inStack)
            if containsCycle:
                return True

        return False

    def isNodeInCycle(self, edges, node, visited, inStack):
        visited[node] = True
        inStack[node] = True

        neighbors = edges[node]
        for neighbor in neighbors:

            if not visited[neighbor]:
 
                containsCycle = self.isNodeInCycle(edges, neighbor, visited, inStack)
                if containsCycle:
                    return True

            elif inStack[neighbor]:
                return True

        inStack[node] = False




# AlgoExpert Solution 2
# O(V + E) time | O(V) space
WHITE, GREY, BLACK = 0, 1, 2


class Solution2:
    def cycleInGraph(self, edges):
        number_of_nodes = len(edges)

        colors = [WHITE for _ in range(number_of_nodes)]

        for node in range(number_of_nodes):
            if colors[node] != WHITE:
                continue

            contains_cycle = self.traverse_and_color_nodes(node, edges, colors)
            if contains_cycle:
                return True

        return False

    def traverse_and_color_nodes(self, node, edges, colors):
        colors[node] = GREY

        neighbors = edges[node]
        for neighbor in neighbors:
            neighbor_color = colors[neighbor]

            if neighbor_color == GREY:
                return True

            if neighbor_color == BLACK:
                continue

            contains_cycle = self.traverse_and_color_nodes(neighbor, edges, colors)
            if contains_cycle:
                return True

        colors[node] = BLACK
        return False


if __name__ == '__main__':
    edges = [
        [1, 3],
        [2, 3, 4],
        [0],
        [],
        [2, 5],
        []
    ]

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.cycleInGraph(edges))
    print(sol2.cycleInGraph(edges))
