import heapq

# O(N + ELog(E)) Time | O(N + E) Space
def dijkstrasAlgorithm(start, edges):
    shortest_paths = [float('inf') for _ in range(len(edges))]

    pq = [(0, start)]
    heapq.heapify(pq)
    shortest_paths[start] = 0

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)

        if curr_distance > shortest_paths[curr_node]:
            continue

        for dest, dist in edges[curr_node]:
            if shortest_paths[dest] > curr_distance + dist:
                shortest_paths[dest] = curr_distance + dist
                heapq.heappush(pq, (shortest_paths[dest], dest))

    for i in range(len(shortest_paths)):
        if shortest_paths[i] == float('inf'):
            shortest_paths[i] = -1

    return shortest_paths


if __name__ == '__main__':
    start = 0
    edges = [
        [
            [1, 7]
        ],
        [
            [2, 6],
            [3, 20],
            [4, 3]
        ],
        [
            [3, 14]
        ],
        [
            [4, 2]
        ],
        [],
        []
    ]

   # print(edges[1][2])
    # for i in range(len(edges)):
    #     for j in range(len(edges[i])):

    #         print(edges[i][j])

    print(dijkstrasAlgorithm(start, edges))