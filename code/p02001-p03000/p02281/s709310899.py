class Node:
    def __init__(self,name):
        self.name=name
        self.root=None
        self.left=None
        self.right=None



def Preorder(node,order):
    order.append(node.name)
    try:
        Preorder(node.left,order)
    except:
        pass
    try:
        Preorder(node.right,order)
    except:
        pass

def Inorder(node,order):
    try:
        Inorder(node.left,order)
        order.append(node.name)
    except:
        order.append(node.name)
    
    try:
        Inorder(node.right,order)
    except:
        pass

def Postorder(node,order):
    try:
        Postorder(node.left,order)
    except:
        pass
    try:
        Postorder(node.right,order)
    except:
        pass
    order.append(node.name)





n=int(input())
Tree=[]
for i in range(n):
    Tree.append(Node(i))


for loop in range(n):
    name,left,right=map(int,input().split())
    if(left!=-1):
        Tree[name].left=Tree[left]
        Tree[left].root=Tree[name]
    if(right!=-1):
        Tree[name].right=Tree[right]
        Tree[right].root=Tree[name]



for i in range(n):
    if(Tree[i].root is None):
        root=Tree[i]


p_order=[]
Preorder(root,p_order)

i_order=[]
Inorder(root,i_order)

po_order=[]
Postorder(root,po_order)

print("Preorder")
print("",end=" ")
print(" ".join(list(map(str,p_order))))

print("Inorder")
print("",end=" ")
print(" ".join(list(map(str,i_order))))

print("Postorder")
print("",end=" ")
print(" ".join(list(map(str,po_order))))
