class Node():
    def __init__(self,parent=-1,left=-1,right=-1,depth=0,height=-1,degree=0,sibling=-1,typ='internal node'):
        self.parent=parent
        self.left=left
        self.right=right
        self.depth=depth
        self.height=height
        self.degree=degree
        self.sibling=sibling
        self.typ=typ
        
def depth(node,i,n):
    node[i].depth=n
    if node[i].left!=-1:
        depth(node,node[i].left,n+1)
    if node[i].right!=-1:
        depth(node,node[i].right,n+1)

def height(node,i):
    hl,hr=0,0
    if node[i].left!=-1:
        height(node,node[i].left)
        hl=node[node[i].left].height+1
    if node[i].right!=-1:
        height(node,node[i].right)
        hr=node[node[i].right].height+1
    node[i].height=max(hl,hr)
    

n=int(input())
N=[Node() for i in range(n)]
for i in range(n):
    p,l,r=[int(i) for i in input().split()]
    if l!=-1:
        N[p].left=l
        N[l].parent=p
        N[p].degree+=1
        if r != -1:
            N[l].sibling=r
            N[r].sibling=l
    if r!=-1:
        N[p].right=r
        N[r].parent=p
        N[p].degree+=1
    elif l==-1 and r==-1:
        N[p].typ='leaf'
        N[p].height=0


for i in range(n):
    height(N,i)
    if N[i].parent==-1:
        N[i].typ='root'
        depth(N,i,0)

for i in range(n):
    print('node '+str(i)+': parent = '+str(N[i].parent)+', sibling = '+str(N[i].sibling)+', degree = '+str(N[i].degree)+', depth = '+str(N[i].depth)+', height = '+str(N[i].height)+', '+N[i].typ)


    
    
