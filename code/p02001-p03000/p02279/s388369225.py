class Node:
	def __init__(self, id):
		self.id = id
		self.parent_id = -1
		self.depth = -1
		self.children = None
	def get_type(self):
		if self.parent_id == -1:
			return 'root'
		elif self.children == None or len(self.children) == 0:
			return 'leaf'
		return 'internal node'
	def __str__(self):
		strNode = 'node ' + str(self.id) + ': '
		strNode += 'parent = ' + str(self.parent_id) + ', '
		strNode += 'depth = ' + str(self.depth) + ', '
		strNode += self.get_type() + ', ['
		if len(self.children) > 0:
			strNode += str(self.children[0])
			for i in range(1, len(self.children)):
				strNode +=  ', ' + str(self.children[i])
		strNode += ']'
		return strNode

def calc_depth(nodes):
	stack = []
	for i in range(len(nodes)):
		if nodes[i].parent_id == -1:
			nodes[i].depth = 0
			stack.append(nodes[i].id)
			break
	while len(stack) != 0:
		node = nodes[stack.pop()]
		for i in range(len(node.children)):
			child_id = node.children[i]
			nodes[child_id].depth = node.depth + 1
			stack.append(child_id)

n = int(input())
nodes = [Node(i) for i in range(n)]
for i in range(n):
	a = list(map(int, input().split()))
	id = a[0]
	node = nodes[id]
	m = a[1]
	children = [0] * m
	for j in range(m):
		child_id = a[2 + j]
		child = nodes[child_id]
		child.parent_id = id
		children[j] = child_id
	node.children = children

calc_depth(nodes)

for i in range(n):
	print(nodes[i])
