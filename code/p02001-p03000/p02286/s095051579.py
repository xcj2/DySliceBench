class Node:
    def __init__(self,key,priority):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None
        self.priority=priority
        self.rightflag=-1


def insert(root,node):#rootを根に持つ２分探索木にnodeを追加する
    if(root.key <= node.key):
        if(root.right is None):
            root.right=node
            node.parent=root
            node.rightflag=1
        else:
            insert(root.right,node)
    
    else:
        if(root.left is None):
            root.left=node
            node.parent=root
            node.rightflag=0
        else:
            insert(root.left,node)


def find(root,key):
    if(root.key==key):
        return root

    elif(root.key < key):
        if(root.right is not None):
            return find(root.right,key)
        else:
            return None

    else:
        if(root.left is not None):
            return find(root.left,key)
        else:
            return None







                   
            
        



    

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



def right_rotate(node,Root):#nodeのparentの場所にnodeを移動させる(二分木の条件を保ちつつ)
    if(node.parent==None):#与えられたnodeがrootだった場合0を返す
        return 0
    
    node.parent.left=node.right#NoneでもこれでOk
    if(node.right is not None):
        node.right.parent=node.parent
        node.right.rightflag=0
    

    if(node.parent.parent is not None):
        tmp_parent=node.parent.parent
        node.parent.parent=node
        node.rightflag=node.parent.rightflag
        node.parent.rightflag=1
        node.right=node.parent
        node.parent=tmp_parent
        if(node.rightflag):
            tmp_parent.right=node
        else:
            tmp_parent.left=node
    else:
        node.parent.parent=node
        node.rightflag=-1
        node.parent.rightflag=1
        node.right=node.parent
        node.parent=None
        Root[0]=node
    
    return 1


def left_rotate(node,Root):#nodeのparentの場所にnodeを移動させる(二分木の条件を保ちつつ)
    if(node.parent==None):#与えられたnodeがrootだった場合0を返す
        return 0
    
    node.parent.right=node.left#NoneでもこれでOk
    if(node.left is not None):
        node.left.parent=node.parent
        node.left.rightflag=1
    

    if(node.parent.parent is not None):
        tmp_parent=node.parent.parent
        node.parent.parent=node
        node.rightflag=node.parent.rightflag
        node.parent.rightflag=0
        node.left=node.parent
        node.parent=tmp_parent
        if(node.rightflag):
            tmp_parent.right=node
        else:
            tmp_parent.left=node
    else:
        node.parent.parent=node
        node.rightflag=-1
        node.parent.rightflag=0
        node.left=node.parent
        node.parent=None
        Root[0]=node
    
    return 1


def delete(Root,key):
    if(Root[0] is None):
        pass
    else:
        target=find(Root[0],key)
        if(target is None):
            pass
        else:
            while( target.left is not None or target.right is not None):
                if(target.left is not None and target.right is not None):
                    if(target.left.priority <= target.right.priority):
                        left_rotate(target.right,Root)
                    else:
                        right_rotate(target.left,Root)
                
                
                elif(target.left is not None):
                    right_rotate(target.left,Root)
                elif(target.right is not None):
                    left_rotate(target.right,Root)        
            
            if(target.rightflag==1):
                target.parent.right=None
            elif(target.rightflag==0):
                target.parent.left=None
            else:
                Root[0]=None


n=int(input())
root=None

for loop in range(n):
    ope=input().split()

    if(ope[0]=="insert"):
        tmp_node=Node(int(ope[1]),int(ope[2]))
        try:
            insert(root,tmp_node)
            Root=[root]
            while(tmp_node.parent.priority <tmp_node.priority):
                if(tmp_node.rightflag):
                    left_rotate(tmp_node,Root)
                else:
                    right_rotate(tmp_node,Root)
            root=Root[0]
        except:
            root=tmp_node

    elif(ope[0]=="rotate"):
        if(root is not None):
            target=find(root,int(ope[1]))
            if(target is not None):
                Root=[root]
                left_rotate(target,Root)
                root=Root[0]
    
    elif(ope[0]=="find"):
        try:
            if(find(root,int(ope[1])) is not None):
                print("yes")

            else:
                print("no")
        except:
            print("no")
    
    elif(ope[0]=="delete"):
        Root=[root]
        delete(Root,int(ope[1]))
        root=Root[0]

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

