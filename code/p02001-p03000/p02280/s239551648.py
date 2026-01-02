from sys import stdin
N=int(input())
nodes=[None]*N
sibling=[None]*N
dep=[0]*N
parent_list=[None]*N
degree=[0]*N
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

def search_depth(u,p):
    dep[u.node]=p
    if u.right is not None and u.left is not None:
        degree[u.node]=2
    elif u.left is not None:
        degree[u.node]=1
    elif u.right is not None:
        degree[u.node] = 1
    else:degree[u.node]=0

    if u.right is not None:
        parent_list[u.right.node]=u.node
        search_depth(u.right,p+1)
    if u.left is not None:
        parent_list[u.left.node]=u.node
        search_depth(u.left,p+1)
def search_height(u):
    h1,h2=0,0
    if u.right is not None:
        h1=search_height(u.right)+1
    if u.left is not None:
        h2=search_height(u.left)+1
    return max(h1,h2)

def search_sib(u):
    if u.brother is not None:
        sibling[u.node]=u.brother.node
        sibling[u.brother.node]=u.node
    if u.left is not None:
        search_sib(u.left)
    if u.right is not None:
        search_sib(u.right)
search_sib(nodes[oya])
search_depth(nodes[oya],0)
word_list=["internal node","leaf"]
for i in range(N):
    height = search_height(nodes[i])
    if height>=1:word=word_list[0]
    else:word=word_list[1]
    if i==oya:
        parent_list[oya]=-1
        sibling[oya]=-1
        word="root"
    if sibling[i] is None:sibling[i]=-1
    print(("node %d: parent = %d, sibling = %d, degree = %d, depth = %d, height = %d, %s" % \
           (nodes[i].node, parent_list[i],sibling[i],degree[i], dep[i], height,word)))
