import sys

class Node():

	def __init__(self,id,k,children):
		
		self.id = id
		self.k = k
		self.children = children
		self.parent = -1
		self.depth = 0

def find_root(Nodes,node):

	if node.parent == -1:
		return node.id

	return find_root(Nodes,Nodes[node.parent])

def define_depth(Nodes,node):

	if node.k == 0: #leaf
		return True

	for child in node.children: #internal node
		Nodes[child].depth = node.depth + 1
		define_depth(Nodes,Nodes[child])

def sort(Nodes):

	for i in range(len(Nodes)-1):
		for j in range(i+1,len(Nodes)):

			if Nodes[i].id > Nodes[j].id:

				Nodes[i],Nodes[j] = Nodes[j],Nodes[i]

def test():

	n = int(sys.stdin.readline())
	child = []
	Nodes = [Node(0,0,child)] * n
	root = 0

	# Reading inputs
	for i in range(n):

		inputs = list(map(int,sys.stdin.readline().split()))
		id = inputs[0]
		k = inputs[1]
		child = []
		for j in range(k):
			child.append(inputs[2+j])

		tmp_node = Node(id,k,child)
		Nodes[id] = tmp_node

	#sort(Nodes)

	# Add "parent" attribute
	for node in Nodes:

		for i in range(node.k):
			
			Nodes[node.children[i]].parent = node.id
	
	# Find "root"
	root = find_root(Nodes,Nodes[0])

	#print(root)

	# Define depth from root
	define_depth(Nodes,Nodes[root])

	for i in range(n):

		print(f"node {Nodes[i].id}: parent = {Nodes[i].parent}, depth = {Nodes[i].depth}, ",end='')

		if Nodes[i].parent == -1:
			print(f"root, [",end='')
		elif Nodes[i].k == 0:
			print(f"leaf, [",end='')
		else:
			print(f"internal node, [",end='')

		for j in range(Nodes[i].k - 1):
			print(f"{Nodes[i].children[j]}, ",end='')
		if Nodes[i].k != 0:
			print(f"{Nodes[i].children[Nodes[i].k-1]}]")
		else:
			print("]")


if __name__ == "__main__":
	test()

