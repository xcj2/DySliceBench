class Node:
	def __init__(self, id):
		self.id = id
		self.parent_id = -1
		self.left = -1
		self.right = -1
		self.sibling = -1
		self.depth = -1
		self.height = -1
	def get_type(self):
		if self.parent_id == -1:
			return 'root'
		elif self.left == -1 and self.right == -1:
			return 'leaf'
		return 'internal node'
	def get_degree(self):
		ret = 0
		if self.left != -1: ret += 1
		if self.right != -1: ret += 1
		return ret
	def __str__(self):
		strNode = 'node ' + str(self.id) + ': '
		strNode += 'parent = ' + str(self.parent_id) + ', '
		strNode += 'sibling = ' + str(self.sibling) + ', '
		strNode += 'degree = ' + str(self.get_degree()) + ', '
		strNode += 'depth = ' + str(self.depth) + ', '
		strNode += 'height = ' + str(self.height) + ', '
		strNode += self.get_type()
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
		if node.left != -1:
			nodes[node.left].depth = node.depth + 1
			stack.append(node.left)
		if node.right != -1:
			nodes[node.right].depth = node.depth + 1
			stack.append(node.right)

def calc_height(nodes):
	stack = []
	for i in range(len(nodes)):
		if nodes[i].left == -1 and nodes[i].right == -1:
			nodes[i].height = 0
			stack.append(nodes[i].id)
	while len(stack) != 0:
		node = nodes[stack.pop()]
		if node.parent_id != -1:
			parent = nodes[node.parent_id]
			parent.height = max(parent.height, node.height + 1)
			stack.append(node.parent_id)

n = int(input())
nodes = [Node(i) for i in range(n)]
for i in range(n):
	id, left, right = map(int, input().split())
	nodes[id].left = left
	nodes[id].right = right
	if left != -1:
		nodes[left].parent_id = id
		nodes[left].sibling = right
	if right != -1:
		nodes[right].parent_id = id
		nodes[right].sibling = left

calc_depth(nodes)
calc_height(nodes)

for i in range(n):
	print(nodes[i])

