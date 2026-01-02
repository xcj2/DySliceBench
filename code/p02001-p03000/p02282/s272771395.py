

class Node:
    def __init__(self,name):
        self.name=name
        self.left=-1
        self.right=-1
        self.parent=-1



def mk_tree(Tree,p_order,in_order):
    tmp_p_order=[]
    tmp_in_order=[]
    root=p_order[0]#p_orderの先頭要素が、rootになる

    root_ind=0    
    while(in_order[root_ind] != root):
        root_ind+=1#in_orderでのrootのindexを返す 



    if(root_ind!=0):
        Tree[root].left=p_order[1]
        Tree[p_order[1]].parent=root
        tmp_in_order=in_order[0:root_ind]
        tmp_p_order=p_order[1:root_ind+1]
        mk_tree(Tree,tmp_p_order,tmp_in_order)

    if(root_ind!=len(p_order)-1):
        Tree[root].right=p_order[root_ind+1]
        Tree[p_order[root_ind+1]].parent=root
        tmp_in_order=in_order[root_ind+1:]
        tmp_p_order=p_order[root_ind+1:]
        mk_tree(Tree,tmp_p_order,tmp_in_order)
    


def Postorder(Tree,root,order):
    if(Tree[root].left!=-1):
        Postorder(Tree,Tree[root].left,order)
    if(Tree[root].right!=-1):
        Postorder(Tree,Tree[root].right,order)
    order.append(root)
       






n=int(input())
p_order=list(map(int,input().split()))
root=p_order[0]
in_order=list(map(int,input().split()))
Tree=[None]
for i in range(n):
   Tree.append(Node(i+1))

mk_tree(Tree,p_order,in_order)

#for i in range(1,n+1):
 #  print(f"id {i}: left = {Tree[i].left}, right = {Tree[i].right}, parent = {Tree[i].parent}")



post_order=[]
Postorder(Tree,root,post_order)
print(" ".join(list(map(str,post_order))))
