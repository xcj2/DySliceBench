import sys


class Node():

	def __init__(self,id,left,right):
		
		self.id = id
		self.left = left
		self.right = right
		self.parent = -1
		self.sibling = -1
		self.degree = 0
		self.depth = 0
		self.height = 0

def define_depth(Nodes,node):

	if node.left == -1 and node.right == -1: #leaf
		return

	if node.left != -1:
		Nodes[node.left].depth = node.depth + 1
		define_depth(Nodes,Nodes[node.left])
	if node.right != -1:
		Nodes[node.right].depth = node.depth + 1
		define_depth(Nodes,Nodes[node.right])

def define_height(Nodes,node):

	h1 = 0
	h2 = 0

	if node.left != -1:
		h1 += define_height(Nodes,Nodes[node.left]) + 1
	if node.right != -1:
		h2 += define_height(Nodes,Nodes[node.right]) + 1

	return max(h1,h2)

def find_root(Nodes,node):

	if node.parent == -1:
		return node.id

	return find_root(Nodes,Nodes[node.parent])

def print_nodes(Nodes,node_id,type,output):

	#TYPE
	#0 : Preorder
	#1 : Inorder
	#2 : Postorder

	if node_id == -1:
		return

	if type == 0:
		output.append(node_id)

	print_nodes(Nodes,Nodes[node_id].left,type,output)
	if type == 1:
		output.append(node_id)
	print_nodes(Nodes,Nodes[node_id].right,type,output)
	if type == 2:
		output.append(node_id)

def test():

	n = int(sys.stdin.readline())
	Nodes = [Node(0,0,0)] * n
	root = 0

	# Reading inputs
	for i in range(n):

		inputs = list(map(int,sys.stdin.readline().split()))
		id = inputs[0]
		left = inputs[1]
		right = inputs[2]

		tmp_node = Node(id,left,right)
		Nodes[id] = tmp_node

	# Defining parent and sibling and root
	for node in Nodes:

		child_count = 0

		# Parent
		if node.right != -1:
			Nodes[node.right].parent = node.id
			child_count += 1
		if node.left != -1:
			Nodes[node.left].parent = node.id
			child_count += 1

		# Degree
		node.degree = child_count

		#Sibling
		if node.right != -1 and node.left != -1:
			Nodes[node.right].sibling = node.left
			Nodes[node.left].sibling = node.right

	# Finding root
	root = find_root(Nodes,Nodes[0])

	# Defining depth
	define_depth(Nodes,Nodes[root])

	# Defining height
	for node in Nodes:
		node.height = define_height(Nodes,node)

	output = []

	# Printing Nodes
	print_nodes(Nodes,Nodes[root].id,0,output)
	print("Preorder")
	for i in range(n):
		print(f" {output[i]}",end='')
	print()
	
	output.clear()
	print_nodes(Nodes,Nodes[root].id,1,output)
	print("Inorder")
	for i in range(n):
		print(f" {output[i]}",end='')
	print()

	output.clear()
	print_nodes(Nodes,Nodes[root].id,2,output)
	print("Postorder")
	for i in range(n):
		print(f" {output[i]}",end='')
	print()

if __name__ == "__main__":
	test()


