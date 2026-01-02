n = int(input())

class Node:
	def __init__(self, index, parent, children):
		self.parent = parent
		self.children = children
		self.depth = -1
		self.index = index
	
	def type(self):
		if self.parent == -1:
			return "root"
		elif len(self.children) == 0:
			return "leaf"
		else:
			return "internal node"
		
nodes = [Node(i, -1,[]) for i in range(n)]

for _ in range(n):
	l = list(map(int, input().split()))
	if l[1] > 0:
		children = l[2:]
		nodes[l[0]].children = children
		for child in children:
			nodes[child].parent = l[0]

def dfs(thisIndex, thisDepth):
	nodes[thisIndex].depth = thisDepth
	for child in nodes[thisIndex].children:
		dfs(child, thisDepth+1)
	

for node in nodes:
	if node.parent == -1:
		depth = 0
		dfs(node.index, 0)
		break
		
for node in nodes:
	print("node {}: parent = {}, depth = {}, {}, {}".format(node.index, node.parent, node.depth, node.type(), node.children))	
