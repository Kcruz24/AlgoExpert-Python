# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(N) time | O(1) space
    def buildHeap(self, array):
        last_idx = len(array) - 1
        first_parent_idx = (last_idx - 1) // 2

        for parent in reversed(range(first_parent_idx + 1)):
            self.siftDown(parent, last_idx, array)

        return array

    # O(log(N)) time | O(1) space
    def siftDown(self, curr_idx, end_idx, heap):
        child_one_idx = 2 * curr_idx + 1

        while child_one_idx <= end_idx:
            child_two_calc = 2 * curr_idx + 2
            child_two_idx = child_two_calc if child_two_calc <= end_idx else -1

            child_one_val = heap[child_one_idx]
            child_two_val = heap[child_two_idx]
            # if there is a second child
            if child_two_idx != -1 and child_two_val < child_one_val:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            
            if heap[idx_to_swap] < heap[curr_idx]:
                self.swap(idx_to_swap, curr_idx, heap)
                curr_idx = idx_to_swap
                child_one_idx = 2 * curr_idx + 1  # Update first child

            else:
                return

    # O(log(N)) time | O(1) space
    def siftUp(self, curr_idx, heap):
        parent_idx = (curr_idx - 1) // 2
        parent_val = heap[parent_idx]
        curr_val = heap[curr_idx]

        while curr_idx > 0 and curr_val < parent_val:
            self.swap(curr_idx, parent_idx, self.heap)

            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2
            parent_val = heap[parent_idx]
            curr_val = heap[curr_idx]

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(N)) time | O(1) space
    def remove(self):
        last_idx = len(self.heap) - 1
        self.swap(0, last_idx, self.heap)
        value_to_remove = self.heap.pop()

        self.siftDown(0, len(self.heap) - 1, self.heap)

        return value_to_remove

    # O(log(N)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        last_idx = len(self.heap) - 1
        self.siftUp(last_idx, self.heap)

    def swap(self, idx_one, idx_two, heap):
        heap[idx_one], heap[idx_two] = heap[idx_two], heap[idx_one]

    def print_heap(self):
        print('Min Heap:', self.heap)


if __name__ == '__main__':
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]

    heap = MinHeap(array)

    heap.print_heap()
    heap.insert(76)
    heap.print_heap()
