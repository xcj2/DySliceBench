import sys


class Node():

	def __init__(self,id,key):
		
		self.id = id
		self.key = key
		self.root = -1
		self.left = -1
		self.right = -1
		self.parent = -1
		self.sibling = -1
		self.degree = 0
		self.depth = 0
		self.height = 0

def print_nodes(Nodes,node_id,type,output):

	#TYPE
	#0 : Preorder
	#1 : Inorder
	#2 : Postorder

	if node_id == -1:
		return

	if type == 0:
		output.append(Nodes[node_id].key)

	print_nodes(Nodes,Nodes[node_id].left,type,output)
	if type == 1:
		output.append(Nodes[node_id].key)
	print_nodes(Nodes,Nodes[node_id].right,type,output)
	if type == 2:
		output.append(Nodes[node_id].key)

def insert(T,z):

	if len(T) == 1:
		return


	y = -1
	x = T[0]

	while True:
		y = x
		if z.key < x.key:
			if x.left == -1:
				break
			else:
				x = T[x.left]
		else:
			if x.right == -1:
				break
			else:
				x = T[x.right]

	z.parent = y.id
	if z.key < y.key:
		y.left = z.id
	else:
		y.right = z.id

def test():

	n = int(sys.stdin.readline())
	T = [Node(0,0)] * n
	root = 0
	id = 0

	for i in range(n):

		inputs = sys.stdin.readline().split()

		if inputs[0] == "insert":
			if id == 0:
				T[id] = Node(id,int(inputs[1]))
				id += 1
				continue

			key = int(inputs[1])
			tmp_node = Node(id,key)
			T[id] = tmp_node
			insert(T,tmp_node)
			id += 1

		if inputs[0] == "print":
			output = []
			#In-order
			print_nodes(T,T[0].id,1,output)
			for j in range(len(output)-1):
				print(f" {output[j]}",end = '')
			print(f" {output[j+1]}")

			#Pre-order
			output2 = []
			print_nodes(T,T[0].id,0,output2)
			for j in range(len(output2)-1):
				print(f" {output2[j]}",end = '')
			print(f" {output2[j+1]}")

if __name__ == "__main__":
	test()

