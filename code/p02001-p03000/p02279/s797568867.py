#再起関数の上限を変更
import sys
sys.setrecursionlimit(2**20)

#クラスの定義
class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def get_depth(T: dict, u: int):
    #Tは木の構造と見立てたdictで、uはTのノード
    d = 0
    while T[u].parent is not None:
        u = T[u].parent
        d += 1

D = {} #深さを保存しておくためのdict

def get_all_depth(T: dict, u: int, p: int):
    #一度に全てのノードの深さを取得する関数(再帰的に処理を行う)。
    #一気に深さを取得するならば、こちらの方がオーダーが小さい
    #pは現在扱う深さ

    D[u] = p
    if T[u].right is not None:
        #まずは兄弟のノードから入れていく
        get_all_depth(T,T[u].right,p)
    if T[u].left is not None:
        # 兄弟を入れ終わったら次は下の深さへ
        get_all_depth(T, T[u].left, p+1)

def ret_children(T,u):
    children = []
    c = T[u].left
    while c is not None:
        children.append(c)
        c = T[c].right

    return children

#答えの出力用

def print_for_a_node(T: dict, node: int, D: dict):
    node_type = 'internal node' if T[node].left is not None else 'leaf'
    #parentを決める
    if T[node].parent == None:
        parent = -1
        node_type = 'root'
    else:
        parent = T[node].parent
    #子を決める
    children = ret_children(T,node)
    print(f'node {node}: parent = {parent}, depth = {D[node]}, {node_type}, {children}')

n = int(input())

#初期化
T = {k: Node(None, None, None) for k in range(n)}
#全てのleft,right,parentを決める
for _ in range(n):
    tmp = list(map(int,input().split()))
    if tmp[1] == 0: #もし子ノードが無ければ次へ
        continue
    T[tmp[0]].left = tmp[2]#子供のノードが分かる
    T[tmp[2]].parent = tmp[0] #子供の親のノードも即座に分かるだろう
    prev_sibiling = tmp[2] #前のノードを覚えておくよう
    #print (tmp)
    for sib in tmp[3:]:
        #print (prev_sibiling,sib)
        T[prev_sibiling].right = sib
        T[sib].parent = tmp[0]  # 子から親を与えている
        prev_sibiling = sib

#print(T[1].right)

for node in range(n):
    #rootからｋ考えなければいけない
    if T[node].parent == None:
        get_all_depth(T,node,0)
        break
    #Dに深さが入った

for node in range(n):
    print_for_a_node(T, node, D)

