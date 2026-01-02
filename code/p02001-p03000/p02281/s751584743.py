#7-C tree walk
class node():
    def __init__(self):
        self.left=-1
        self.right=-1
        self.parent=-1

def preorder(i):
    print(' '+str(i),end='')
    if nodes[i].left!=-1:
        preorder(nodes[i].left)
    if nodes[i].right!=-1:
        preorder(nodes[i].right)
    
def inorder(i):
    if nodes[i].left!=-1:
        inorder(nodes[i].left)
    print(' '+str(i),end='')
    if nodes[i].right!=-1:
        inorder(nodes[i].right)
        
def postorder(i):
    if nodes[i].left!=-1:
        postorder(nodes[i].left)
    if nodes[i].right!=-1:
        postorder(nodes[i].right)
    print(' '+str(i),end='')
  

n=int(input())
nodes=[node() for i in range(n)]
for i in range(n):
    p,l,r=[int(i) for i in input().split()]
    nodes[p].left=l
    nodes[p].right=r
    if l!=-1:nodes[l].parent=p
    if r!=-1:nodes[r].parent=p

root=-1
for i in range(n):
    if nodes[i].parent==-1:
        root=i
        break

print('Preorder')
preorder(root)
print()

print('Inorder')
inorder(root)
print()

print('Postorder')
postorder(root)
print()


