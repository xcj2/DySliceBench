#AGC039-B
"""
二部グラフで無いなら分割はできない。
二部グラフの場合、頂点間の最も長い距離＋１
が答え。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
g = [[float("inf")]*n for i in range(n)]
g2 = [[] for i in range(n)] #g[i]:点iに隣接している点のリスト
for i in range(n):
    s = readline().rstrip().decode('utf-8')
    for j in range(n):
        if s[j] == "1":
            g[i][j] = 1
            g2[i].append(j)
            g2[j].append(i)
for i in range(n):
    g[i][i] = 0 #自分自身への距離は0とする

def warshall_floyd(d): #隣接行列を入れる
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

FW = warshall_floyd(g)

color = [0] * n #color[i]:点iの色(1 or -1)。但し塗られていないときは0とする

def f(v,c,g):
    #頂点vに隣接する頂点全てを塗るあるいは判定する
    color[v] = c
    for i in range(len(g[v])):
        if color[ g[v][i] ] == c:
            return False
        elif color[ g[v][i] ] == 0 and not f(g[v][i],-c,g2):
            #(g[v][i]がまだ塗られていない　かつ　そこを-cで塗っても問題ない) ではないなら
            return False
    return True

k = 1 #判定　1ならYes -1ならNo
for i in range(n):
    if color[i] == 0:
        if not f(i,1,g2):
            k = -1

if k != 1:
    print(-1)
else:
    ans = 0
    for i in FW:
        for j in i:
            if j != float("inf"):
                ans = max(ans,j)
    print(ans+1)