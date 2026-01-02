class Node():
	def __init__(self, key):
		self.parent = None
		self.left = None
		self.right = None
		self.key = key
 
class Tree():
	def __init__(self):
		self.root = None
	def insert(self, key):
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
	def out(self):
		self.in_order(self.root)
		print("")
		self.pre_order(self.root)
		print("")
	def find(self, key):
		node = self.root;
		while node:
			if node.key == key:
				return "yes"
			elif node.key > key:
				node = node.left
			else:
				node = node.right
		return "no"

tree = Tree()
n = int(input())
for i in range(n):
	c = input().split()
	if c[0] == "insert":
		tree.insert(int(c[1]))
	elif c[0] == "find":
		print(tree.find(int(c[1])))
	else:
		tree.out()