# Tree walk 木の巡回


class Node():
    
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1


def preordertreewalk(u):
    print(" ", u, end="", sep="")
    if T[u].left != -1:
        preordertreewalk(T[u].left)
    if T[u].right != -1:
        preordertreewalk(T[u].right)


def inordertreewalk(u):
    if T[u].left != -1:
        inordertreewalk(T[u].left)
    print(" ", u, end="", sep="")
    if T[u].right != -1:
        inordertreewalk(T[u].right)


def postordertreewalk(u):
    if T[u].left != -1:
        postordertreewalk(T[u].left)
    if T[u].right != -1:
        postordertreewalk(T[u].right)
    print(" ", u, end="", sep="")


n = int(input())
T = [Node() for i in range(n)]
for i in range(n):
    id, left, right = (int(d) for d in input().split())
    if left != -1:
        T[id].left = left
        T[left].parent = id
    if right != -1:
        T[id].right = right
        T[right].parent = id

rootid = -1
for id in range(n):
    if T[id].parent == -1:
        rootid = id

print("Preorder")
preordertreewalk(rootid)

print("\nInorder")
inordertreewalk(rootid)

print("\nPostorder")
postordertreewalk(rootid)
print()

