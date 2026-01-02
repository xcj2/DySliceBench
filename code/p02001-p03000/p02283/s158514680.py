from typing import List, Optional


class Node:
	def __init__(self, key) -> None:
		self.key: int = key
		self.left: Optional[Node] = None
		self.right: Optional[Node] = None
		self.parent: Optional[Node] = None


class Tree:
	def __init__(self) -> None:
		self.root: Optional[Node] = None


def insert(T: Tree, z: Node) -> None:
	y: Optional[Node] = None
	x: Optional[Node] = T.root
	while x is not None:
		y = x # 親を設定
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.parent = y

	if y is None:
		T.root = z
	elif z.key < y.key:
		y.left = z
	else:
		y.right = z


def inorder(z: Optional[Node]):
	if z is not None:
		inorder(z.left)
		print(f" {z.key}", end="")
		inorder(z.right)


def preorder(z: Optional[Node]):
	if z is not None:
		print(f" {z.key}", end="")
		preorder(z.left)
		preorder(z.right)


if __name__ == "__main__":
	m = int(input())
	T = Tree()
	for _ in range(m):
		command = list(input().split())
		if command[0] == "insert":
			z = Node(int(command[1]))
			insert(T, z)
		else:
			inorder(T.root)
			print("")
			preorder(T.root)
			print("")
