from sys import setrecursionlimit
setrecursionlimit(100000000)

NIL = -1
n = int(input())
class Node:
    def __init__(self, p, l, r, s=-1, c=0, d=0, h=0, t='nil'):
        self.p = p 
        self.l = l
        self.r = r
        self.s = s
        self.c = c
        self.d = d
        self.h = h
        self.t = t

T = [Node(NIL, NIL, NIL) for _ in range(n)]
#入力から二分木の情報を受け取る 
for _ in range(n):
    data = [int(i) for i in input().split()]
    node_id = data[0]
    cl = data[1]
    cr = data[2]
    T[node_id].l = cl
    T[node_id].r = cr
    cnt_child = 0
    if cl != NIL:
        T[cl].p = node_id
        T[cl].s = cr
        cnt_child += 1
    if cr != NIL:
        T[cr].p = node_id
        T[cr].s = cl
        cnt_child += 1
    T[node_id].c = cnt_child 

#node id: parent = p, sibling = s, degree = deg, height = h, typeを出力するプログラムを作る

def setDepth(node_id, depth):
    T[node_id].d = depth
    l = T[node_id].l
    r = T[node_id].r
    if l != NIL:
        setDepth(l, depth+1)
    if r != NIL:
        setDepth(r, depth+1)

#rootのノードを探す関数
def searchRoot():
    for i in range(n):
        if T[i].p == NIL:
            return i
    return 

#高さを求める関数
#sovelHeight関数はnode_idの高さを返す関数
def solveHeight(node_id):
    hl = 0
    hr = 0
    #node_idから子を辿る
    if T[node_id].l != NIL: 
        hl = solveHeight(T[node_id].l)+1
    if T[node_id].r != NIL:
        hr = solveHeight(T[node_id].r)+1
    res = max(hl, hr)
    T[node_id].h = res
    return res


#nodeの種類を求める関数
def nodeType(node_id):
    if T[node_id].p == NIL:
        T[node_id].t = 'root'
        return  

    if (T[node_id].l == NIL) and (T[node_id].r == NIL):
        T[node_id].t = 'leaf'
        return 
    #rootでもleafでもないnodeはindternal nodeである
    T[node_id].t = 'internal node'

#全てのnodeの種類を決める
def allNodeTypeDiff():
    for i in range(n):
        nodeType(i)

#node_idのノードの情報をprintする
def nodeInfo(node_id):
    p = T[node_id].p
    s = T[node_id].s
    c = T[node_id].c
    d = T[node_id].d
    h = T[node_id].h
    t = T[node_id].t
    node_info = "node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(node_id, p, s, c, d, h, t)
    print(node_info)
#全てのノードの情報をprintする
def allNodeInfo():
    for i in range(n):
        nodeInfo(i)

def main():
    root = searchRoot()
    solveHeight(root)
    setDepth(root, 0)
    allNodeTypeDiff()
    allNodeInfo()
main()
