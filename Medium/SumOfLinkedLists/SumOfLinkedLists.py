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
    new_linked_list = LinkedList(0)
    travNode = new_linked_list
    carry_over = 0

    node_one = linkedListOne
    node_two = linkedListTwo
    while node_one is not None or node_two is not None or carry_over != 0:
        value_one = node_one.value if node_one is not None else 0
        value_two = node_two.value if node_two is not None else 0

        sum_of_values = value_one + value_two + carry_over

        new_value = sum_of_values % 10
        new_node = LinkedList(new_value)

        travNode.next = new_node
        travNode = new_node

        carry_over = sum_of_values // 10

        node_one = node_one.next if node_one is not None else None
        node_two = node_two.next if node_two is not None else None

    return new_linked_list.next


if __name__ == '__main__':
    ll1 = LinkedList(2).addMany([4, 7, 1])
    ll2 = LinkedList(9).addMany([4, 5])
    expected = LinkedList(1).addMany([9, 2, 2])
    actual = sumOfLinkedLists(ll1, ll2)
    print(getNodesInArray(actual) == getNodesInArray(expected))
