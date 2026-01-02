class Node:
	def __init__(self):
		self.p = self.l = self.r = -1

def pre_order(nodes, u):
	if u == -1: return
	print(' ' + str(u), end='')
	pre_order(nodes, nodes[u].l)
	pre_order(nodes, nodes[u].r)

def in_order(nodes, u):
	if u == -1: return
	in_order(nodes, nodes[u].l)
	print(' ' + str(u), end='')
	in_order(nodes, nodes[u].r)

def post_order(nodes, u):
	if u == -1: return
	post_order(nodes, nodes[u].l)
	post_order(nodes, nodes[u].r)
	print(' ' + str(u), end='')

n = int(input())
nodes = []
for i in range(n): nodes.append(Node())
for i in range(n):
	id, l, r = map(int, input().split())
	nodes[id].l = l
	nodes[id].r = r
	if l != -1: nodes[l].p = id
	if r != -1: nodes[r].p = id
for i in range(n):
	if nodes[i].p == -1:
		rootId = i
		break
print('Preorder')
pre_order(nodes, rootId)
print()
print('Inorder')
in_order(nodes, rootId)
print()
print('Postorder')
post_order(nodes, rootId)
print()

