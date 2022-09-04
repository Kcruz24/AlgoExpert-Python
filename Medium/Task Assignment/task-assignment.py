'''

k = 3
tasks = [1, 3, 5, 3, 1, 4]

[1, 5] = 6
[1, 4] = 5
[3, 3] = 6
'''
import heapq


def taskAssignment(k, tasks):
    if min(tasks) == max(tasks):
        return [[i, i + 1] for i in range(0, k * 2, 2)]

    min_tasks = []
    max_tasks = []

    for idx, task in enumerate(tasks):
        heapq.heappush(min_tasks, (task, idx))
        heapq.heappush(max_tasks, (-task, idx))

    optimal = []

    while k:
        _, min_idx = heapq.heappop(min_tasks)
        _, max_idx = heapq.heappop(max_tasks)

        if min_idx == max_idx:
            _, min_idx = heapq.heappop(min_tasks)

        optimal.append([min_idx, max_idx])

        k -= 1

    return optimal


if __name__ == '__main__':
    k = 3
    tasks = [1, 3, 5, 3, 1, 4]

    print(taskAssignment(k, tasks))

    k = 5
    tasks = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(taskAssignment(k, tasks))
