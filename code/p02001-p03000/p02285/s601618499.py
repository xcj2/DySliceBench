class Node:
	def __init__(self, key):
		self.key = key
		self.left = self.right = self.parent = None

class BST:
	def __init__(self):
		self.root = None
	
	def insert(self, key):
		parent = None
		current = self.root
		while current != None:
			parent = current
			if key < current.key:
				current = current.left
			else:
				current = current.right
		new = Node(key)
		new.parent = parent
		if parent == None:
			self.root = new
		elif key < parent.key:
			parent.left = new
		else:
			parent.right = new		
	
	def find(self, key):
		current = self.root
		while current != None:
			if key == current.key:
				return current
			if key < current.key:
				current = current.left
			else:
				current = current.right
		return None
		
	def delete(self, key):
		target = self.find(key)
		if target == None:
			return

		parent = target.parent
		if target.left == None or target.right == None:
			child = None
			if target.left != None:
				child = target.left
			elif target.right != None:
				child = target.right
			
			if child != None:
				child.parent = parent
	
			if parent == None:
				self.root = child
			elif parent.left == target:
				parent.left = child
			else:
				parent.right = child
		else:
			current = target.right
			while current.left != None:
				current = current.left
			target.key = current.key
			parent = current.parent
			if current.right != None:
				parent.left = current.right
				current.right.parent = parent
			else:
				if parent.left == current:
					parent.left = None
				else:
					parent.right = None
	
	def print(self):
		self.print_in_order(self.root)
		print()
		self.print_pre_order(self.root)
		print()
		
	def print_in_order(self, node):
		if node != None:
			self.print_in_order(node.left)
			print(' ' + str(node.key), end='')
			self.print_in_order(node.right)
		
	def print_pre_order(self, node):
		if node != None:
			print(' ' + str(node.key), end='')
			self.print_pre_order(node.left)
			self.print_pre_order(node.right)		

n = int(input())
bst = BST()
for i in range(n):
	cmd = list(map(str, input().split()))
	if cmd[0] == 'print':
		bst.print()
	else:
		key = int(cmd[1])
		if cmd[0] == 'insert':
			bst.insert(key)
		elif cmd[0] == 'find':
			if bst.find(key) != None:
				print('yes')
			else:
				print('no')
		else:
			bst.delete(key)

