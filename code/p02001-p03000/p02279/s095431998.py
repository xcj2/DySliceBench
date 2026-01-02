class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

#ノードの深さを求める関数
def getdepth(node,node_id):
    d = 0
    while node[node_id].parent != -1:
        node_id = node[node_id].parent
        d += 1
    return d

#子のリストを求める関数
def getchild(node,node_id):
    if node[node_id].left == -1:
        return []
    ret = [node[node_id].left]
    while node[ret[-1]].right != -1:
        ret.append(node[ret[-1]].right)
    return ret

N = int(input())
nodes = [Node() for i in range(N)]

#入力を木構造に入力する
for i in range(N):
    n,k,*child = map(int,input().split())
    if k != 0:
        nodes[n].left = child[0]
        for j in range(len(child)):
            nodes[child[j]].parent = n
            if j != len(child)-1:
                nodes[child[j]].right = child[j+1]

for i in range(N):
    depth = getdepth(nodes,i)
    children = getchild(nodes,i)
    if nodes[i].parent == -1:
        node_type = 'root'
    elif nodes[i].left == -1:
        node_type = 'leaf'
    else:
        node_type = 'internal node'
    print('node {}: parent = {}, depth = {}, {}, {}'.format(i,nodes[i].parent, depth, node_type, children))

