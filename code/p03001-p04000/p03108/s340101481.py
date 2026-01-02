import sys
input = sys.stdin.readline

# 組み合わせ　n_C_r
def comb(n,r):
    r = min(r,n-r)
    result = 1
    for i in range(n-r+1,n+1):
        result *= i
    for i in range(1,r+1):
        result //= i
    return result

def root(x):
    # ノードが負 <=> xは根
    if nodes[x] < 0:
        return x
    else:
        # 経路圧縮:再帰的に根を調べてその過程で通った要素は全て根に直接つなぎ直す
        nodes[x] = root(nodes[x])
        return nodes[x]

def unite(x,y):
    root_x = root(x); root_y = root(y)
    # 根が同じなら結合済みなのでreturn(わざわざ分岐するのは自己ループを考慮)
    if root_x == root_y:
        return
    # 根ノードは木の高さを表す(負数で表していることに注意)
    rank_x = -nodes[root_x]; rank_y = -nodes[root_y]
    if rank_x >= rank_y:
        root_l = root_x; root_s = root_y
    else:
        root_l = root_y; root_s = root_x
    # 繋いだ分だけ木を高くする
    nodes[root_l] += nodes[root_s]
    # 低い木を高い木に繋げる
    nodes[root_s] = root_l

def same(x,y):
    return root(x) == root(y)

def rank(x):
    return -nodes[root(x)]

N,M = map(int,input().split())
info = [list(map(int,input().split())) for i in range(M)]

# ノードは-1で初期化, Nは頂点数
nodes = [-1]*N
ans_list = [comb(N,2)]
ans = comb(N,2)
for i in range(1,M)[::-1]:
    A = info[i][0]-1; B = info[i][1]-1
    if not(same(A,B)):
        ans -= rank(A)*rank(B)
    unite(A,B)
    ans_list.append(ans)

for e in ans_list[::-1]:
    print(e)