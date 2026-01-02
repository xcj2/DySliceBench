# ALDS1_7_C Tree Walk
import sys


class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.parent = -1


def preorder(A, i, B):
    B.append(i)
    if A[i].left != -1:
        preorder(A, A[i].left, B)
    if A[i].right != -1:
        preorder(A, A[i].right, B)
    return


def inorder(A, i, B):
    if A[i].left != -1:
        inorder(A, A[i].left, B)
    B.append(i)
    if A[i].right != -1:
        inorder(A, A[i].right, B)
    return


def postorder(A, i, B):
    if A[i].left != -1:
        postorder(A, A[i].left, B)
    if A[i].right != -1:
        postorder(A, A[i].right, B)
    B.append(i)
    return


n = int(input())

tree = []
for i in range(n):
    node = Node()
    tree.append(node)

root = [i for i in range(n)]
for i in range(n):
    A = list(map(int, sys.stdin.readline().strip().split()))
    tree[A[0]].left = A[1]
    tree[A[0]].right = A[2]

    if A[1] != -1:
        tree[A[1]].parent = A[0]
        root.remove(A[1])
    if A[2] != -1:
        tree[A[2]].parent = A[0]
        root.remove(A[2])

print('Preorder')
ans = []
preorder(tree, root[0], ans)
print('', ' '.join(map(str, ans)))

print('Inorder')
ans = []
inorder(tree, root[0], ans)
print('', ' '.join(map(str, ans)))

print('Postorder')
ans = []
postorder(tree, root[0], ans)
print('', ' '.join(map(str, ans)))

