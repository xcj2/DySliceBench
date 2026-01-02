import sys
sys.setrecursionlimit(8388608)
N=int(input())
nodes=[None]*(N+1)
childs=[]
oya=[]
class node_tree:
    def __init__(self,node):
        self.node=node
        self.left=None
        self.right=None
        self.oya=None
for i in range(N):
    node,child_num,*child=list(map(int,input().split()))
    if nodes[node] is not None:
        parent=nodes[node]
    else:
        parent=node_tree(node)
    if child_num>=1:
        if nodes[child[0]] is not None:
            tree=nodes[child[0]]
        else:
            tree=node_tree(child[0])
        parent.left=tree
        tree.oya=parent
        nodes[node]=parent
        nodes[child[0]]=tree
        for j in range(len(child)-1):
            if nodes[child[j]] is not None:
                treesecond=nodes[child[j]]
            else:
                treesecond=node_tree(child[j])
            if nodes[child[j+1]] is not None:
                treenext = nodes[child[j+1]]
            else:
                treenext = node_tree(child[j+1])
            treesecond.oya=parent
            treenext.oya=parent
            treesecond.right=treenext
            nodes[child[j]]=treesecond
            nodes[child[j+1]]=treenext
    else:
        parent.left=nodes[-1]
        nodes[node]=parent
def oyasearch(u):
    if u.oya is not None:
        oyasearch(u.oya)
    else:
        oya.append(u.node)
oyasearch(nodes[0])
dep=[0]*N
parent_list=[None]*N
parent_list[oya[0]]=-1
child_list=[]
def search_depth(u,p):
    dep[u.node]=p
    if u.right is not None:
        parent_list[u.right.node]=parent_list[u.node]
        search_depth(u.right,p)
    if u.left is not None:
        parent_list[u.left.node]=u.node
        search_depth(u.left,p+1)
search_depth(nodes[oya[0]],0)
def child_search(u,c):
    c.append(u.node)
    if u.right is not None:
        child_search(u.right,c)
for i in range(N):
    c=[]
    if nodes[i].left is not None:
        child_search(nodes[i].left,c)
    child_list.append(c)
word_list=["internal node","leaf"]
for i in range(N):
    if i==oya[0]:
        print(("node %d: parent = %d, depth = %d, root," % (nodes[oya[0]].node, parent_list[oya[0]], dep[oya[0]])),
              child_list[oya[0]])
    else:
        if len(child_list[i])!=0:
            word=word_list[0]
        else:word=word_list[1]
        print(("node %d: parent = %d, depth = %d, %s," % (nodes[i].node, parent_list[i], dep[i],word)), child_list[i])

