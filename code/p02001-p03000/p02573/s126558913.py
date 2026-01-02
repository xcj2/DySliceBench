"""
UnionFindにはいろいろな実装があるが, 本問ではparents配列にノード数を保持する実装だと非常に簡単に解ける. 
以下のようにしてノード数を保持する.
自身が子のとき, 親ノード番号を格納する.
自身が根のとき, ノード数を負の数で格納する.
つまり,　負の数のときは自身が根であり, その絶対値がその木のノード数を表す.
初期化時は、すべてのノードを−1で初期化する.
"""

N,M = map(int,input().split())

#UnionFind木の実装
#-1で初期化し、併合のたびに-1していく
par = [-1] * N  #親
rank = [0] * N #木の深さ

#木の根を求める
def find(x):
    #par[x]が負のとき(自分が代表のとき)、自身を返す
    if par[x] < 0:
        return x
    else:
        return find(par[x])

#xとyの属する集合を併合
def unite(x,y):
    x = find(x)
    y = find(y)
    #もとから同じ集合のときは何もしない
    if (x == y):
        return
    #x側を常に小さくする
    if par[x] > par[y]:
            x, y = y, x
    
    #x側に併合する、その際xの代表にノード数を加算する
    par[x] += par[y]
    par[y] = x
    

#xとyが同じ集合に属するかどうか
def same(x,y):
    return find(x) == find(y)

for i in range(M):
    x,y = map(int,input().split())
    x -= 1; y -= 1
    unite(x,y)


ans = min(par)

print(abs(ans))
