# ALDS1_7_B Binary Tree
import sys


class Node:
    def __init__(self):
        self.parent = -1
        self.left = None
        self.right = None
        self.height = None
        self.depth = None
        self.sibling = -1
        self.type = 'internal node'
        self.deg = 0


def calc_depth(A, i):
    if A[i].depth:
        return A[i].depth

    if A[i].parent == -1:
        A[i].depth = 0
    else:
        A[i].depth = calc_depth(A, A[i].parent) + 1
    return A[i].depth


def calc_height(A, i):
    if A[i].height:
        return A[i].height

    if (A[i].left == -1) & (A[i].right == -1):
        A[i].height = 0
        return A[i].height

    if A[i].left == -1:
        A[i].height = calc_height(A, A[i].right) + 1
    elif A[i].right == -1:
        A[i].height = calc_height(A, A[i].left) + 1
    else:
        A[i].height = max(calc_height(A, A[i].left), calc_height(A, A[i].right)) + 1

    return A[i].height


n = int(input())

tree = []
for i in range(n):
    node = Node()
    tree.append(node)

for i in range(n):
    A = list(map(int, sys.stdin.readline().strip().split()))
    tree[A[0]].left = A[1]
    tree[A[0]].right = A[2]
    if A[1] != -1:
        tree[A[1]].parent = A[0]
        tree[A[1]].sibling = A[2]
        tree[A[0]].deg += 1
    if A[2] != -1:
        tree[A[2]].parent = A[0]
        tree[A[2]].sibling = A[1]
        tree[A[0]].deg += 1
    if (A[1] == -1) & (A[2] == -1):
        tree[A[0]].type = 'leaf'

for i in range(n):
    calc_depth(tree, i)
    height = calc_height(tree, i)
    if tree[i].parent == -1:
        node_type = 'root'
    else:
        node_type = tree[i].type

    print('node {}: parent = {}, sibling = {},'
          ' degree = {}, depth = {}, height = {}, {}'.format(i, tree[i].parent, tree[i].sibling,
                                                             tree[i].deg, tree[i].depth, height,
                                                             node_type))


