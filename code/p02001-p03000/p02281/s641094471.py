from sys import stdin
N=int(input())
nodes=[None]*N
class node_tree():
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
        self.brother=None
        self.up=None
for i in range(N):
    node,left,right = list(map(int, (stdin.readline().strip().split())))
    if nodes[node] is not None:
        parent=nodes[node]
    else:parent=node_tree(node)
    if left!=-1:
        if nodes[left] is not None:
            left_node=nodes[left]
        else:left_node=node_tree(left)
        parent.left=left_node
        left_node.up=parent

    if right!=-1:
        if nodes[right] is not None:
            right_node=nodes[right]
        else:right_node=node_tree(right)
        parent.right=right_node
        right_node.up=parent
    if left!=-1 and right!=-1:
        left_node.brother=right_node
        right_node.brother=left_node
    if left!=-1:
        nodes[left] = left_node
    if right!=-1:
        nodes[right] = right_node
    nodes[node]=parent

def search_root(u):
    if u.up!=None:
        return search_root(u.up)
    else:
        return u.node
oya=search_root(nodes[0])
print("Preorder")
def pre(u):
    print("",u.node,end="")
    if u.left is not None:
        pre(u.left)
    if u.right is not None:
        pre(u.right)
pre(nodes[oya])
print("\nInorder")
def ino(u):

    if u.left is not None:
        ino(u.left)
    print("",u.node,end="")
    if u.right is not None:
        ino(u.right)
ino(nodes[oya])
print("\nPostorder")
def pos(u):

    if u.left is not None:
        pos(u.left)
    if u.right is not None:
        pos(u.right)
    print("",u.node,end="")
pos(nodes[oya])
print()
