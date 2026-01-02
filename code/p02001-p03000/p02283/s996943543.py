class Node:
	def __init__(self, k):
		self.k = k
		self.l = self.r = self.p = None
	def __str__(self):
		return str(self.k)

class BST:
	def __init__(self):
		self.root = None
	
	def insert(self, node):
		p = None
		cur = self.root
		while cur != None:
			p = cur
			if node.k < cur.k:
				cur = cur.l
			else:
				cur = cur.r
		node.p = p			
		if p == None:
			self.root = node
		elif node.k < p.k:
			p.l = node
		else:
			p.r = node
	
	def print(self):
		self.print_in_order()
		self.print_pre_order()
	
	def print_in_order(self):
		st = []
		cur = self.root
		while cur != None or len(st) != 0:
			if cur != None:
				st.append(cur)
				cur = cur.l
			else:
				cur = st.pop()
				print(' ' + str(cur), end='')
				cur = cur.r
		print()
		
	def print_pre_order(self):
		st = []
		st.append(self.root)
		while len(st) != 0:
			cur = st.pop()
			print(' ' + str(cur), end='')
			if cur.r != None:
				st.append(cur.r)
			if cur.l != None:
				st.append(cur.l)
		print()

m = int(input())
bst = BST()
for i in range(m):
	cmd = list(map(str, input().split()))
	if cmd[0] == 'insert':
		bst.insert(Node(int(cmd[1])))
	else:
		bst.print()

