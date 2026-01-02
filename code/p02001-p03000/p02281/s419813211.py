# coding: utf-8
# Your code here!

class Node:
    def __init__(self):
        self.parentId=-1
        self.left=-1
        self.right=-1

def preorder(id):
    global node
    print(" "+str(id),end="")
    if node[id].left != -1:
        preorder(node[id].left)
    if node[id].right != -1:
        preorder(node[id].right)
    
def inorder(id):
    global node
    if node[id].left != -1:
        inorder(node[id].left)
    print(" "+str(id),end="")
    if node[id].right != -1:
        inorder(node[id].right)

def postorder(id):
    global node
    if node[id].left !=-1:
        postorder(node[id].left)
    if node[id].right!=-1:
        postorder(node[id].right)
    print(" "+str(id),end="")

n=int(input())
a=[[int(i)for i in input().split()]for j in range(n)]
node=[Node()for i in range(n)]

for i in a:
    id=i[0]
    left=i[1]
    right=i[2]
    node[id].left=left
    node[id].right=right
    if left != -1:node[left].parentId=id
    if right != -1:node[right].parentId =id

root=-1
for i in range(n):
    if node[i].parentId==-1:
        root=i
        break
print("Preorder")
preorder(root)
print("\nInorder")
inorder(root)
print("\nPostorder")
postorder(root)
print("")
