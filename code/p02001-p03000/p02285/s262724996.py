class Node():
	def __init__(self, key):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key
 
class Tree():
	def __init__(self):
		self.root = None
	def insert_node(self, key):
		z = Node(key)
		y = None
		x = self.root
		while x:
			y = x
			if z.key < x.key:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == None:
			self.root = z;
		elif z.key < y.key:
			y.left = z
		else:
			y.right = z
	def delete_node(self, key):
		node = self.find_node(key)
		if node.left and node.right:
			right_min = node.right
			while right_min.left:
				right_min = right_min.left
			node.key = right_min.key
			node = right_min
		if node.left or node.right:
			child = node.left if node.left else node.right
			if node.parent.left == node:
				node.parent.left = child
				child.parent = node.parent
			else:
				node.parent.right = child
				child.parent = node.parent
		else:
			if node.parent.left == node:
				node.parent.left = None
			else:
				node.parent.right = None

	def pre_order(self, node):
		print(" {}".format(node.key), end = "")
		if node.left:
			self.pre_order(node.left)
		if node.right:
			self.pre_order(node.right)
	def in_order(self, node):
		if node.left:
			self.in_order(node.left)
		print(" {}".format(node.key), end = "")
		if node.right:
			self.in_order(node.right)
	def print_node(self):
		self.in_order(self.root)
		print("")
		self.pre_order(self.root)
		print("")
	def find_node(self, key):
		node = self.root;
		while node:
			if node.key == key:
				return node
			elif node.key > key:
				node = node.left
			else:
				node = node.right
		return None

tree = Tree()
n = int(input())
for i in range(n):
	c = input().split()
	if c[0] == "insert":
		tree.insert_node(int(c[1]))
	elif c[0] == "find":
		print("yes" if tree.find_node(int(c[1])) else "no")
	elif c[0] == "delete":
		tree.delete_node(int(c[1]))
	else:
		tree.print_node()