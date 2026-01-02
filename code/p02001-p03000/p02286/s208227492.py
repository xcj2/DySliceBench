# coding:utf-8

NIL =  None

class Node():
	def __init__(self, key, pri):
		self.key = key
		self.pri = pri
		self.right = NIL
		self.left = NIL


def rightRotate(t):
	s = t.left
	t.left = s.right
	s.right = t
	return s

def leftRotate(t):
	s = t.right
	t.right = s.left
	s.left = t
	return s

def insert(t, key, pri):
	if t == NIL:
		return Node(key, pri)
	if key == t.key:
		return t

	if key < t.key:
		t.left = insert(t.left, key, pri)
		if t.pri < t.left.pri:
			t = rightRotate(t)
	else :
		t.right = insert(t.right, key, pri)
		if t.pri < t.right.pri:
			t = leftRotate(t)

	return t

def erase(t, key):
	if t == NIL:
		return NIL
	if key == t.key:
		if t.right == NIL and t.left == NIL:
			return NIL
		elif t.left == NIL:
			t = leftRotate(t)
		elif t.right == NIL:
			t = rightRotate(t)
		else :
			if t.left.pri > t.right.pri:
				t = rightRotate(t)
			else :
				t = leftRotate(t)
		return erase(t, key)

	if key < t.key:
		t.left = erase(t.left, key)
	else:
		t.right = erase(t.right, key)

	return t

def find(t, key):
	if t == NIL:
		return False
	if key == t.key:
		return True

	if key < t.key:
		return find(t.left, key)
	else:
		return find(t.right, key)


head = Node(-1, 2000000001)

def print_priorder(t):
	if t == NIL:
		return

	if t != head:
		print(" " + str(t.key), end='')

	print_priorder(t.left)
	print_priorder(t.right)

def print_inorder(t):
	if t == NIL:
		return

	print_inorder(t.left)
	if t != head:
		print(" " + str(t.key), end='')
	print_inorder(t.right)


n = int(input()) # 命令の数

for i in range(n):
	inst = input().split()

	if inst[0] == "insert":
		insert(head, int(inst[1]), int(inst[2]))

	elif inst[0] == "find":
		if find(head, int(inst[1])):
			print("yes")
		else :
			print("no")

	elif inst[0] == "delete":
		erase(head, int(inst[1]))

	elif inst[0] == "print":
		print_inorder(head)
		print()
		print_priorder(head)
		print()
