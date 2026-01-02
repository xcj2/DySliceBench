class Node:
	def __init__(self):
		self.parent = -1
		self.left = -1
		self.right = -1

# T : List[Node]

def preOrder(id: int):
	left_id = T[id].left
	right_id = T[id].right
	print(" " + str(id), end="")
	if left_id != -1:
		preOrder(left_id)
	if right_id != -1:
		preOrder(right_id)

def inOrder(id: int):
	left_id = T[id].left
	right_id = T[id].right
	if left_id != -1:
		inOrder(left_id)
	print(" " + str(id), end="")
	if right_id != -1:
		inOrder(right_id)

def postOrder(id: int):
	left_id = T[id].left
	right_id = T[id].right
	if left_id != -1:
		postOrder(left_id)
	if right_id != -1:
		postOrder(right_id)
	print(" " + str(id), end="")


if __name__ == "__main__":
	n = int(input())
	T = []
	for i in range(n):
		T.append(Node())
	for i in range(n):
		id, left, right = map(int, input().split())
		T[id].left = left
		T[id].right = right
		if left != -1:
			T[left].parent = id
		if right != -1:
			T[right].parent = id

	for i in range(n):
		if T[i].parent == -1:
			root_id = i
	print("Preorder")
	preOrder(root_id)
	print("")
	print("Inorder")
	inOrder(root_id)
	print("")
	print("Postorder")
	postOrder(root_id)
	print("")
