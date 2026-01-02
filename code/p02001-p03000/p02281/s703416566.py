class Node:
	def __init__(self):
		self.p = self.l = self.r = -1

def pre_order(nodes, root_id):
	st = []
	st.append(root_id)
	while len(st) > 0:
		cur = st.pop()
		print(' ' + str(cur), end='')
		if nodes[cur].r != -1: st.append(nodes[cur].r)
		if nodes[cur].l != -1: st.append(nodes[cur].l)
	print()
	
def in_order(nodes, root_id):
	st = []
	cur = root_id
	while cur != -1 or len(st) > 0:
		if cur != -1:
			st.append(cur)
			cur = nodes[cur].l
		else:
			cur = st.pop()
			print(' ' + str(cur), end='')
			cur = nodes[cur].r
	print()
		
def post_order(nodes, root_id):
	st = []
	lastVisited = -1
	cur = root_id
	while cur != -1 or len(st) > 0:
		if cur != -1:
			st.append(cur)
			cur = nodes[cur].l
		else:
			peek_id = st[len(st) - 1]
			if nodes[peek_id].r != -1 and nodes[peek_id].r != lastVisited:
				cur = nodes[peek_id].r
			else:
				print(' ' + str(peek_id), end='')
				lastVisited = st.pop()
	print()

n = int(input())
nodes = [Node() for x in range(n)]
for i in range(n):
	id, l, r = map(int, input().split())
	nodes[id].l = l
	nodes[id].r = r
	if l != -1: nodes[l].p = id
	if r != -1: nodes[r].p = id
for i in range(n):
	if nodes[i].p == -1:
		root_id = i
		break

print('Preorder')
pre_order(nodes, root_id)
print('Inorder')
in_order(nodes, root_id)
print('Postorder')
post_order(nodes, root_id)

