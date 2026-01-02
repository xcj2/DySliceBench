class Node:
    def __init__(self):
        self.name=-1
        self.parent=-1
        self.children=[]
        self.degree=0
        self.depth=-1
        self.state="leaf"
        self.sibling=-1
        self.height=-1




def get_depth(Tree,node,depth):
    for child in node.children:
        Tree[child].depth=depth+1
        get_depth(Tree,Tree[child],depth+1)


def get_height(Tree):
    for node in Tree:
        if(len(node.children)==0):
                node.height=0
                tmp_node=node
                while(tmp_node.parent!=-1):
                        Tree[tmp_node.parent].height=max([tmp_node.height+1, Tree[tmp_node.parent].height])
                        tmp_node=Tree[tmp_node.parent]
                     




Tree=[]
n=int(input())
for i in range(n):
    Tree.append(Node())
for loop in range(n):
    info=list(map(int,input().split()))
    i=info[0]
    Tree[i].name=i
    for j in range(1,len(info)):
        if(info[j]!=-1):
                (Tree[i].children).append(info[j])
                if(info[1]!=-1 and info[2]!=-1):
                        Tree[info[2]].sibling=info[1]
                        Tree[info[1]].sibling=info[2]
                Tree[i].state="internal node"
                Tree[info[j]].parent=i




for node in Tree:
    if(node.parent==-1):
        node.state="root"
        node.depth=0
        get_depth(Tree,node,0)


get_height(Tree)
        


for node in Tree:
    print(f"node {node.name}: parent = {node.parent}, sibling = {node.sibling}, degree = {len(node.children)}, depth = {node.depth}, height = {node.height}, {node.state}")

