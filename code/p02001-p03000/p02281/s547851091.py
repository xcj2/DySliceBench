# coding: utf-8
# Your code here!


null = -1

class Node:
    def __init__(self):
        self.parent = null
        self.left = null
        self.right = null
        self.id = null
    

def preParse(u):
    if u == null:
        return
    print(" ", end = "")
    print(Tree[u].id, end = "")
    preParse(Tree[u].left)
    preParse(Tree[u].right)
    
def inParse(u):
    if u == null:
        return
    inParse(Tree[u].left)
    print(" ", end = "")
    print(Tree[u].id, end = "")
    inParse(Tree[u].right)
    
def postParse(u):
    if u == null:
        return
    postParse(Tree[u].left)
    postParse(Tree[u].right)
    print(" ", end = "")
    print(Tree[u].id, end = "")


Tree = []
root = 0

n = int(input())
for i in range(n):
    Tree.append(Node())
    
for i in range(n):
    tmp = list(map(int, input().split()))
    
    Tree[tmp[0]].id = tmp[0]
    
    if tmp[1] != -1:
        Tree[tmp[0]].left = tmp[1]
        Tree[tmp[1]].parent = tmp[0]
    if tmp[2] != -1:
        Tree[tmp[0]].right = tmp[2]
        Tree[tmp[2]].parent = tmp[0]

for i in range(n):
    if Tree[i].parent == null:
        root = i
        break

print("Preorder\n", end = "")
preParse(root)
print("\nInorder")
inParse(root)
print("\nPostorder")
postParse(root)
print("")
    











