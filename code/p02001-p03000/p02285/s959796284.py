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


def parent_search(tree,node):
    parent=None
    child=root
    while child is not None and child!=node:
        parent=child
        if node<child:child=tree[parent][0]
        else:child=tree[parent][1]
    return parent


def getMinimum(node):
    while tree[node][0] is not None:
        node=tree[node][0]
    return node


def getSuccessor(node):
    if tree[node][1] is not None:
        return getMinimum(tree[node][1])
    target=parent_search(tree,node)
    while target is not None and node==tree[target][1]:
        node=target
        target=parent_search(tree,target)
    return target


def delete(tree,node):
    if tree[node][0] is None or tree[node][1] is None:target=node
    else:target=getSuccessor(node)

    if tree[target][0] is not None:child=tree[target][0]
    else:child=tree[target][1]

    child_parent=parent_search(tree,target)
    if target==tree[child_parent][0]:tree[child_parent][0]=child
    else:tree[child_parent][1]=child
    if target==node:
        del tree[node]
        return

    node_parent=parent_search(tree,node)
    if node==tree[node_parent][0]:tree[node_parent][0]=target
    else:tree[node_parent][1]=target
    tree[target]=tree[node]
    del tree[node]


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
    elif order[0]=="delete":
        delete(tree,int(order[1]))
    elif order[0]=="insert":
        num=int(order[1])
        if root is None:
            root=num
            tree[root]=[None,None]
        else:
            tree[num]=[None,None]
            insert(tree,num)
