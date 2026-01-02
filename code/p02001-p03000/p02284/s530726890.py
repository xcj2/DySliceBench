def insert(tree,node):
    parent=None
    child=root
    while child is not None:
        parent=child
        if node<child:child=tree[parent][0]
        else:child=tree[parent][1]
    if node<parent:tree[parent][0]=node
    else:tree[parent][1]=node


def In_order(node):
    if node is None:return
    In_order(tree[node][0])
    print(" {}".format(node), end="")
    In_order(tree[node][1])


def Pre_order(node):
    if node is None:return
    print(" {}".format(node), end="")
    Pre_order(tree[node][0])
    Pre_order(tree[node][1])


def find(x,key):
    while x is not None and key!=x:
        if key<x:x=tree[x][0]
        else:x=tree[x][1]
    return x


n=int(input())
tree,root={},None
for i in range(n):
    order=input().split()
    if order[0]=="print":
        In_order(root);print()
        Pre_order(root);print()
    elif order[0]=="find":
        if find(root,int(order[1])) is not None:print("yes")
        else:print("no")
    elif order[0]=="insert":
        num=int(order[1])
        if root is None:
            root=num
            tree[root]=[None,None]
        else:
            tree[num]=[None,None]
            insert(tree,num)
