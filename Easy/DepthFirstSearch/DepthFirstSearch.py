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
		

graph = Node("A")
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")	
graph.children[2].children[0].addChild("K")

print(graph.depthFirstSearch([]))