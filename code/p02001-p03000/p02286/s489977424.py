
class Node:
	def __init__(self, key, pri):
		self.key = key
		self.pri = pri
		self.left = self.right = None
	def __str__(self):
		ret = ''
		ret += 'key=' + str(self.key)
		ret += ',pri=' + str(self.pri)
		ret += ',left='
		if self.left != None: ret += str(self.left.key)
		ret += ',right='
		if self.right != None: ret += str(self.right.key)
		return ret

class Treap:
	def __init__(self):
		self.root = None

	def print(self):
		self.print_in_order()
		self.print_pre_order()

	def print_in_order(self):
		st = []
		cur = self.root
		while cur != None or len(st) != 0:
			if cur != None:
				st.append(cur)
				cur = cur.left
			else:
				cur = st.pop()
				print(' ' + str(cur.key), end='')
				cur = cur.right
		print()

	def print_pre_order(self):
		st = []
		st.append(self.root)
		while len(st) != 0:
			cur = st.pop()
			print(' ' + str(cur.key), end='')
			if cur.right != None:
				st.append(cur.right)
			if cur.left != None:
				st.append(cur.left)
		print()

	def find(self, key):
		cur = self.root
		while cur != None:
			if key == cur.key:
				return cur
			if key < cur.key:
				cur = cur.left
			else:
				cur = cur.right
		return None

	def insert(self, key, pri):
		self.root = self.insert_(self.root, key, pri)

	def insert_(self, node, key, pri):
		if node == None:
			return Node(key, pri)
		if key == node.key:
			return node

		if key < node.key:
			node.left = self.insert_(node.left, key, pri)
			if node.pri < node.left.pri:
				node = self.right_rotate(node)
		else:
			node.right = self.insert_(node.right, key, pri)
			if node.pri < node.right.pri:
				node = self.left_rotate(node)
		return node

	def right_rotate(self, node):
		tmp = node.left
		node.left = tmp.right
		tmp.right = node
		return tmp

	def left_rotate(self, node):
		tmp = node.right
		node.right = tmp.left
		tmp.left = node
		return tmp

	def delete(self, key):
		self.root = self.delete_(self.root, key)

	def delete_(self, node, key):
		if node == None:
			return node
		if key < node.key:
			node.left = self.delete_(node.left, key)
		elif key > node.key:
			node.right = self.delete_(node.right, key)
		else:
			return self.delete__(node, key)
		return node

	def delete__(self, node, key):
		if (node.left == None and node.right == None):
			return None
		elif node.left == None:
			node = self.left_rotate(node)
		elif node.right == None:
			node = self.right_rotate(node)
		else:
			if node.left.pri > node.right.pri:
				node = self.right_rotate(node)
			else:
				node = self.left_rotate(node)
		return self.delete_(node, key)

n = int(input())
treap = Treap()
for i in range(n):
	cmd = list(map(str, input().split()))
	if cmd[0] == 'print':
		treap.print()
	else:
		key = int(cmd[1])
		if cmd[0] == 'insert':
			treap.insert(key, int(cmd[2]))
		elif cmd[0] == 'find':
			if treap.find(key) != None:
				print('yes')
			else:
				print('no')
		else:
			treap.delete(key)

