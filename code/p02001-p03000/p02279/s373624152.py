import sys
sys.setrecursionlimit(100000000)

#存在しないノードにはNILを割り当てる
NIL = -1

n = int(input())

#左子右兄弟表現で根つき木を実装していく
class Node:
    def __init__(self, p, l, r):
        self.p = p
        self.l = l
        self.r = r
        self.d = 0
        self.t = 'undifined'
        self.c = []

#T[i]にはノードiの情報を保持する
T = [Node(NIL, NIL, NIL) for _ in range(n)]

#ノードの情報を受け取りTに保持していく
for _ in range(n):
    data = [int(i) for i in input().split()]
    node_id = data[0]
    node_d = data[1]
    child = data[2:]
    if len(child) > 0:
        T[node_id].l = child[0]
    for i in range(len(child)):
        if i < len(child)-1:
            T[child[i]].r = child[i+1]
        T[child[i]].p = node_id
        T[node_id].c.append(child[i])



#仕様
#ノード番号　親ノードの番号　ノードのふかさ　ノードの種類　子ノードのリスト　をノード0から順に出力する

#ノードの深さを求める関数
def setDepth(root_id, depth):
    T[root_id].d = depth
    l = T[root_id].l
    r = T[root_id].r
    if l != NIL:
        setDepth(l, depth+1)
    if r != NIL:
        setDepth(r, depth)

#rootの番号を求める関数
def getRoot():
    for i in range(n):
        p = T[i].p
        if p == NIL:
            return i

#ノードの種類を求める関数
def setNodeType(node_id):
    #親がNILならばrootで確定する
    if T[node_id].p == NIL:
        T[node_id].t = 'root'
        return
    #親が存在して、子が存在しない場合はleaf
    if T[node_id].l == NIL:
        T[node_id].t = 'leaf'
        return 
    #それ以外はinternal node
    T[node_id].t = 'internal node'

def allSetNodeType():
    for i in range(n):
        setNodeType(i)

def outPutNodeInfo(node_id, p_node_id, depth='nil', node_type='nil', child_list='nil'):
    res = "node {}: parent = {}, depth = {}, {}, {}".format(node_id, p_node_id, depth, node_type, child_list)
    print(res)


#問題の答えを出力するための関数
def outPutAns():
    for i in range(n):
        node_id = i
        p_node_id = T[i].p
        depth = T[i].d
        node_type = T[i].t
        child_list = T[i].c
        outPutNodeInfo(node_id, p_node_id, depth, node_type, child_list)



def main():
    setDepth(getRoot(), 0)
    allSetNodeType()
    outPutAns()
main()
