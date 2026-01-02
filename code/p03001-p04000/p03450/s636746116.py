def prepare(n):
    global nodes,diff_weight
    # ノードは-1で初期化, Nは頂点数
    nodes = [-1]*n
    # 差分重みは0で初期化, Nは頂点数
    diff_weight = [0]*n

# 差分重みの累積和をとることでxの重みが分かる
def weight(x):
    # xの重みを知りたいので経路圧縮
    root(x)
    return diff_weight[x]

# xからyへの重み
def diff(x,y):
    return weight(y) - weight(x)

# x,yの根が同じ->True
def same(x,y):
    return root(x) == root(y)

# xの木の高さを返す
def rank(x):
    return -nodes[x]

def root(x):
    # ノードが負 <=> xは根
    if nodes[x] < 0:
        return x
    else:
        # 再帰的に根を調べる
        root_x = root(nodes[x])
        # 根に近いものから親の重みを足す. これがxを根に直接繋いだ時の重みになる
        diff_weight[x] += diff_weight[nodes[x]]
        # xを根に直接繋ぎ直す
        nodes[x] = root_x
        return root_x

def unite(x,y,w):
    # 以下x,yの根について考えるので,重みを補正
    w += weight(x); w -= weight(y)
    x = root(x); y = root(y)
    # 根が同じならreturn (自己ループを考慮)
    if x == y:
        return
    rank_x = rank(x); rank_y = rank(y)
    # xの方が木が高いことを想定しているのでx,yをスワップ,wを-wに
    if rank_x < rank_y:
        x,y = y,x; w = -w
    # 木の高さが同じ場合は繋いだ後の高さが1だけ高くなる
    if rank_x == rank_y:
        nodes[x] -= 1
    # 低い木の根を高い木の根に繋ぎ直す
    nodes[y] = x
    # 低い木の根の差分重みを設定
    diff_weight[y] = w

N,M = map(int,input().split())
prepare(N)
ans = "Yes"
for _ in range(M):
    L,R,D = map(int,input().split())
    L -= 1; R -= 1
    unite(L,R,D)
    if diff(L,R) != D:
        ans = "No"
print(ans)