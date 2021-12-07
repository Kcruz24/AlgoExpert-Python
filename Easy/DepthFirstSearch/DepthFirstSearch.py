class Node:
	def __init__(self, name):
		self.children = []
		self.name = name
		
	def addChild(self, name):
		self.children.append(Node(name))
		return self
		
	# O(V + E) time | O(V) space
	def depthFirstSearch(self, array):
		array.append(self.name)
		for child in self.children:
			child.depthFirstSearch(array)
		return array

	# O(v + e) time | O(v) space
	def depthFirstSearchIterative(self, array):
		stack = [self]
		while len(stack) != 0:
			node = stack.pop()
			array.append(node.name)
			for i in range (len(node.children)-1, -1, -1):
				stack.append(node.children[i])
		return array
		
if __name__ == '__main__':
	graph = Node("A")
	graph.addChild("B").addChild("C").addChild("D")
	graph.children[0].addChild("E").addChild("F")
	graph.children[2].addChild("G").addChild("H")
	graph.children[0].children[1].addChild("I").addChild("J")	
	graph.children[2].children[0].addChild("K")

	print(graph.depthFirstSearchIterative([]) == ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"])

	