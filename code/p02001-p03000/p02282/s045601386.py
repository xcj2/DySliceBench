class Node:
	def __init__(self):
		self.parent = None
		self.left = None
		self.right = None

def restoreTree(preList, inList):
	root = preList[0]
	index = inList.index(root)
	leftin = inList[:index]
	# print(leftin)
	rightin = inList[index + 1:]
	# print(rightin)
	num_left = len(leftin)
	num_right = len(rightin)
	if num_left != 0:
		leftpre = preList[1:1 + num_left]
		# print(leftpre)
		left_root = leftpre[0]
		T[root].left = left_root
		T[left_root].parent = root
		restoreTree(leftpre, leftin)
	if num_right != 0:
		rightpre = preList[1 + num_left:]
		# print(rightpre)
		right_root = rightpre[0]
		T[root].right = right_root
		T[right_root].parent = root
		restoreTree(rightpre, rightin)


def postOrder(root):
	if T[root].left is not None:
		postOrder(T[root].left)
	if T[root].right is not None:
		postOrder(T[root].right)
	L.append(str(root))

if __name__ == "__main__":
	n = int(input())
	T = []
	for _ in range(n + 1):
		T.append(Node())
	preList = list(map(int, input().split()))
	inList = list(map(int, input().split()))
	root = preList[0]
	restoreTree(preList, inList)
	L = []
	postOrder(root)
	print(" ".join(L))
