class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None


def insert(root,node):#rootを根に持つ２分探索木にnodeを追加する
    if(root.key <= node.key):
        if(root.right is None):
            root.right=node
        else:
            insert(root.right,node)
    
    else:
        if(root.left is None):
            root.left=node
        else:
            insert(root.left,node)


def Preorder(root,order):
    order.append(root.key)
    if(root.left is not None):
        Preorder(root.left,order)
    
    if(root.right is not None):
        Preorder(root.right,order)




def Inorder(root,order):
    if(root.left is not None):
        Inorder(root.left,order)
    
    order.append(root.key)

    if(root.right is not None):
        Inorder(root.right,order)




n=int(input())

root=None

for loop in range(n):
    ope=input().split()

    if(ope[0]=="insert"):
        tmp_node=Node(int(ope[1]))
        try:
            insert(root,tmp_node)
        except:
            root=tmp_node
    
    else:
        in_order=[]
        p_order=[]
        
        Inorder(root,in_order)
        Preorder(root,p_order)

        for x in in_order:
            print(f" {x}",end="")
        print()
        for x in p_order:
            print(f" {x}",end="")
        print()
