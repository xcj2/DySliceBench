import sys
sys.setrecursionlimit(1000000)

#ノードの数,橋の数
N,M = map(int, input().split())

#最初は自分自身が親（根）
par = [i for i in range(N+1)]
#ランク(深さ）
rank = [0]*(N+1)
#各要素が属するグループのサイズ（連結成分の個数）
size = [1]*(N+1)

#木の根を求める
def root(x):
    if par[x] == x:  #自分が親のときは自分が根ということ
        return x
    else:
        #経路圧縮
        par[x] = root(par[x])#自分が親ではないときは，根を自分の親に設定
        return par[x]

#xとyが同じ集合（連結成分）に属するかどうか
def same(x, y):
    return root(x) == root(y)

#xとyの属する集合を併合
def unite(x,y):
    xx = root(x)
    yy = root(y)
    #xとyのルートが同じなので操作は必要ない（同じ集合に属する）
    if xx == yy:
        return
    ####ランクあり
    if rank[xx] < rank[yy]:
        par[xx] = yy
        size[yy] += size[xx]
    else:
        par[yy] = xx
        size[xx] += size[yy]
        if rank[xx] == rank[yy]:
            rank[yy] += 1

    ####ランクなし
    ###
    ### #ｘとyのrootが異なるので,xの親をyのrootに設定
    #par[x] = yy

#出力する不便度
ans = [0]*M
#すべての橋が壊れているときの不満度はN個の島から2個の島の選び方の総数と等しい
ans[M-1] = N*(N-1)//2

#橋の情報
B = [list(map(int,input().split())) for i in range(M)]

#橋の情報を逆順に取り出す
for i in range(M-1,0,-1):
    a = B[i][0]
    b = B[i][1]
    if root(a) != root(b):
        ans[i-1] = ans[i] -size[root(a)]*size[root(b)]
    else:
        ans[i-1] = ans[i]
    #橋をつなげる
    unite(a,b)

for a in ans:
    print(a)
