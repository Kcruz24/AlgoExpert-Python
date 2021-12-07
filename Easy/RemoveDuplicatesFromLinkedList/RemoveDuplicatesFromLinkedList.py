# O(N) time | O(1) space
def removeDuplicatesFromLinkedList(linkedList):
	travNode = linkedList
	
	while travNode is not None:
		while travNode.next is not None and travNode.value == travNode.next.value:
			travNode.next = travNode.next.next
		
		travNode = travNode.next

	return linkedList