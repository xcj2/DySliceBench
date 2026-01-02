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


def find(k: int) -> Optional[Node]:
	z = T.root
	while z is not None:
		if k == z.key:
			return z
		elif k < z.key:
			z = z.left
		else:
			z = z.right
	return None

def tree_minimum(x: Node) -> Node:
	while x.left is not None:
		x = x.left
	return x


def tree_successor(x: Node) -> Node:
	if x.right is not None:
		return tree_minimum(x.right)
	y: Optional[Node] = x.parent
	while y is not None and x == y.right:
		x = y
		y = y.parent
	return y


def delete(z: Node) -> None:
	x: Optional[Node] = None
	y: Optional[Node] = None
	if (z.left is None or z.right is None):
		y = z
	else:
		y = tree_successor(z)
	if y.left is not None:
		x = y.left
	else:
		x = y.right
	if x is not None:
		x.parent = y.parent
	if y.parent is None:
		T.root = x
	elif y == y.parent.left:
		y.parent.left = x
	else:
		y.parent.right = x
	if y != z:
		z.key = y.key

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
		elif command[0] == "find":
			key = int(command[1])
			z = find(key)
			if z is not None:
				print("yes")
			else:
				print("no")
		elif command[0] == "delete":
			key = int(command[1])
			z = find(key)
			if z is not None:
				delete(z)
		else:
			inorder(T.root)
			print("")
			preorder(T.root)
			print("")
