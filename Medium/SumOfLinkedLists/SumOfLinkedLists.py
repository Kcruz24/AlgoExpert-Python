class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self


def getNodesInArray(output):
    nodes = []
    current = output
    while current is not None:
        nodes.append(current.value)
        current = current.next
    return nodes


# Algo Expert
# O(max(N, M)) time | O(max(N, M)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):

    result = LinkedList(0)
    result_ptr = result
    carry_over = 0

    while linkedListOne is not None or linkedListTwo is not None or carry_over != 0:
        value_one = linkedListOne.value if linkedListOne is not None else 0
        value_two = linkedListTwo.value if linkedListTwo is not None else 0

        sum_of_values = value_one + value_two + carry_over

        remainder = sum_of_values % 10

        new_linked_list = LinkedList(remainder)
        result_ptr.next = new_linked_list

        carry_over = sum_of_values // 10

        linkedListOne = linkedListOne.next if linkedListOne is not None else None
        linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None
        result_ptr = result_ptr.next

    return result.next


if __name__ == '__main__':
    ll1 = LinkedList(2).addMany([4, 7, 1])
    ll2 = LinkedList(9).addMany([4, 5])
    expected = LinkedList(1).addMany([9, 2, 2])
    actual = sumOfLinkedLists(ll1, ll2)
    print(getNodesInArray(actual) == getNodesInArray(expected))
