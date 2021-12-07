# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        #self.heap = self.buildHeap(array)
        self.heap = array

    def buildHeap(self, array):
        # Write your code here.
        pass

    def siftDown(self):
        # Write your code here.
        pass

    def siftUp(self, cur_idx, heap):
        # Write your code here.
        parent_idx = (cur_idx - 1) // 2
        while cur_idx > 0 and heap[parent_idx] > heap[cur_idx]:
            self.swap(cur_idx, parent_idx, heap)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]
        

    def remove(self):
        # Write your code here.
        return

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, idx_one, idx_two, heap):
        heap[idx_one], heap[idx_two] = heap[idx_two], heap[idx_one]

    def toString(self):
        print(self.heap)





if __name__ == '__main__':
    array = [8, 12, 23, 17, 31, 30, 44, 102, 18]

    min_heap = MinHeap(array)

    min_heap.toString()

    min_heap.insert(9)

    min_heap.toString()

    min_heap.insert(5)

    min_heap.toString()








