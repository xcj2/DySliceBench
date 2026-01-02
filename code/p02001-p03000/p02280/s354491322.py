class Node:
	def __init__(self):
		self.parent = -1
		self.type = "internal node"
		self.sibling = -1
		self.degree = 2
		self.height = 0
		self.left = -1
		self.right = -1
		self.depth = 0

def setDepth(id, depth):
	global T
	T[id].depth = depth
	left = T[id].left
	right = T[id].right
	if left != -1:
		setDepth(left, depth + 1)
	if right != -1:
		setDepth(right, depth + 1)


def setHeight(H: int, u: int):
	global T
	h1 = 0
	h2 = 0
	if T[u].right != -1:
		h1 = setHeight(H, T[u].right) + 1
	if T[u].left != -1:
		h2 = setHeight(H, T[u].left) + 1
	height = max(h1, h2)
	T[u].height = height
	return height


if __name__ == "__main__":
	n = int(input())
	T = []
	for _ in range(n):
		T.append(Node())
	for _ in range(n):
		id, left, right = map(int, input().split())
		T[id].left = left
		T[id].right = right
		if left != -1:
			T[left].sibling = right
			T[left].parent = id
		if right != -1:
			T[right].sibling = left
			T[right].parent = id
	
	for i in range(n):
		if T[i].left == -1:
			T[i].degree -= 1
		if T[i].right == -1:
			T[i].degree -= 1
		if T[i].left == -1 and T[i].right == -1:
			T[i].type = "leaf"
		if T[i].parent == -1:
			root_id = i
			T[i].type = "root"

	setDepth(root_id, 0)
	setHeight(0, root_id)

	for i in range(n):
		node = T[i]
		print(f"node {i}: parent = {node.parent}, sibling = {node.sibling}, degree = {node.degree}, depth = {node.depth}, height = {node.height}, {node.type}")
