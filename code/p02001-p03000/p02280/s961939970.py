# coding: utf-8
# Your code here!

class Node:
    def __init__(self):
        self.parentId=-1
        self.sibling=-1
        self.children=[]
        self.degree=0
        self.depth=-1
        self.height=-1
        self.type=""
        
def calcDepth(x,depth):
    global node
    node[x].depth=depth
    for i in node[x].children:
        calcDepth(i,depth+1)

def calcHeight(x,height):
    global node
    node[x].height=max([height,node[x].height])
    if node[x].parentId != -1:
        calcHeight(node[x].parentId,height+1)

n=int(input())
a=[[int(i)for i in input().split()]for j in range(n)]
node=[Node()for i in range(n)]

for i in a:
    id=i[0]
    left=i[1]
    right=i[2]
    node[id].children=[left,right]
    if left != -1:node[left].sibling,node[left].parentId=right,id
    if right != -1:node[right].sibling,node[right].parentId =left,id

for i in node:
    while -1 in i.children:
        i.children.remove(-1)

for i in node:
    i.degree=len(i.children)

for i in range(n):
    if node[i].parentId==-1:
        calcDepth(i,0)
        break

for i in range(n):
    if node[i].degree==0:
        calcHeight(i,0)

for i in node:
    if i.parentId == -1:
        i.type="root"
    elif i.height==0:
        i.type="leaf"
    else:
        i.type="internal node"


for i in range(n):
    print("node "+str(i)+": parent = "+str(node[i].parentId)+", sibling = "+str(node[i].sibling)+", degree = "+str(node[i].degree)+", depth = "+str(node[i].depth)+", height = "+str(node[i].height)+", "+node[i].type)
