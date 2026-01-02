import sys
sys.setrecursionlimit(2**20)

class Node:
    def __init__(self, parent, left, right):
        self.parent = parent
        self.left = left
        self.right = right

def get_depth(T, u): # T : ノードの情報が入っているdict, u :Node
    d = 0
    while T[u].parent != None:   # TはNodeクラスで作る
        u = T[u].parent     # 親がNIL（つまり根）になるまで親を辿っていく
        d += 1
    return d

D = {}

def get_all_depth(T, u, p):  # p : 深さ
    D[u] = p
    if T[u].right != None:
        get_all_depth(T, T[u].right, p)
    if T[u].left != None:
        get_all_depth(T, T[u].left, p+1)
        
def get_children(T, u):
    children = []
    c = T[u].left
    while c != None:
        children.append(c)
        c = T[c].right
    return children


# 入力
n = int(input()) # Node（節点）の数
T = {i : Node(None, None, None) for i in range(n)} # 情報を入れるdictをNodeクラスで作成

for _ in range(n):   # 変数名を「 _ 」にすることによって、「その変数を使っていない」ことを表現している（Pythonの習慣）
    tmp = list(map(int, input().split())) # Nodeの情報を格納[節点の番号, 次数, 1番目の子の節点番号, ..., k番目の子の節点番号]
    if tmp[1] == 0:  # 子Nodeがなければ次へ 
        continue
    T[tmp[0]].left = tmp[2] # 今見ているNode（tmp[0]）のleftアトリビュートに左子Nodeを入れる
    T[tmp[2]].parent = tmp[0]  # 当然tmp[2]の親はtmp[0]
    prev_sibling = tmp[2]  # 兄弟の一番左のNode番号を保存しておく
    for sib in tmp[3:]:  # 残りの兄弟について
        T[prev_sibling].right = sib  # 一つ右の兄弟 
        T[sib].parent = tmp[0]  # 親は同じくtmp[0]（当然）
        prev_sibling = sib
        
# 出力
def print_for_a_node(T, node, D):
    if T[node].left == None:
        node_type = "leaf"
    else:
        node_type = "internal node"
    
    if T[node].parent == None:
        parent = -1
        node_type = "root"
    else:
        parent = T[node].parent
    
    children = get_children(T, node)

        
    #print(f"node {node} : parent = {parent}, depth = {D[node]}, {node_type}, {children}")
    print("node {}: parent = {}, depth = {}, {}, {}".format(node, parent, D[node], node_type, children))

for node in range(n):
    if T[node].parent == None:
        get_all_depth(T, node, 0)  # rootを入れる
        # Dに深さが入る
        break
        
for node in range(n):
    print_for_a_node(T, node, D)

