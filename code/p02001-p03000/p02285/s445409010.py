class Node:
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None


def insert(root,node):#rootを根に持つ２分探索木にnodeを追加する
    if(root.key <= node.key):
        if(root.right is None):
            root.right=node
            node.parent=root
        else:
            insert(root.right,node)
    
    else:
        if(root.left is None):
            root.left=node
            node.parent=root
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






def delete(Root,key):
    root=Root[0]
    target=find(root,key)#targetは削除対象のnode
    if(target is None):
        pass

    elif(target.parent is None):
        return 0



    else:
        parent=target.parent

        if(parent.key <= target.key):
            right=1
        else:
            right=0
        #targetがparentの右の子の時はright=1、左の子の時はright=0

        if((target.left is None) and (target.right is None)):
            if(right):
                parent.right=None
            else:
                parent.left=None

        elif(target.left is None):
            target.right.parent=parent
            if(right):
                parent.right=target.right
            else:
                parent.left=target.right

        elif(target.right is None):
            target.left.parent=parent
            if(right):
                parent.right=target.left
            else:
                parent.left=target.left
        
        else:
            tmp_min=target.right
            while(tmp_min.left is not None):#targetの右の子を根とする部分木の中で最小のnodeを見つける
                tmp_min=tmp_min.left
            
            if(tmp_min.parent.key <=tmp_min.key):#最小値が、targetの右の子だった場合
                if(right):
                    parent.right=tmp_min
                else:
                    parent.left=tmp_min
                tmp_min.parent=parent
                tmp_min.left=target.left
                target.left.parent=tmp_min
                return 1
            
            if(tmp_min.right is not None):#tmpが右の子を持っていた時の処理
                tmp_min.parent.left=tmp_min.right
                tmp_min.right.parent=tmp_min.parent
            
            tmp_min.parent.left=None
            tmp_min.left=target.left
            target.left.parent=tmp_min
            tmp_min.right=target.right
            target.right.parent=tmp_min
            tmp_min.parent=parent
            if(right):
                parent.right=tmp_min
            else:
                parent.left=tmp_min
    return 1

                   
            
        



    

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
        if(delete(Root,int(ope[1])) ==0):
            root=None

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
