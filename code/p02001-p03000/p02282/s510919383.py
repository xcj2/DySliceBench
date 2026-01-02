class Node:
	def __init__(self, v):
		self.v = v
		self.l = self.r = None
		self.p = -1
	def __str__(self):
		return str(self.v)

def find_pos(a, v):
	for i in range(len(a)):
		if a[i] == v:
			return i
	return -1

def add_node(root, cur, ino):
	cur.p = find_pos(ino, cur.v)
	st = []
	st.append(root)
	while len(st) != 0:
		node = st.pop()
		if node.p == -1:
			node.p = find_pos(ino, node.v)
		if cur.p < node.p:
			if node.l == None:
				node.l = cur
				return
			else:
				st.append(node.l)
		else:
			if node.r == None:
				node.r = cur
				return
			else:
				st.append(node.r)		

def post_order(root):
	st = []
	cur = root
	last = None
	ret = ''
	while cur != None or len(st) != 0:
		if cur != None:
			st.append(cur)
			cur = cur.l
		else:
			peek = st[len(st)-1]
			if peek.r != None and peek.r != last:
				cur = peek.r
			else:
				if len(ret) != 0:
					ret += ' '
				ret += str(peek)
				last = st.pop()
	return ret

n = int(input())
preo = list(map(int, input().split()))
ino = list(map(int, input().split()))
root = Node(preo[0])
for i in range(1, n):
	add_node(root, Node(preo[i]), ino)
print(post_order(root))
