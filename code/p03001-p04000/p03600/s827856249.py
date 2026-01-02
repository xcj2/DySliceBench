import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

import copy

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    arr = copy.deepcopy(d)
    n = len(arr)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
    return arr

def main(): 
    N = II()
    tizu = []
    for _ in range(N):
        tizu.append(LI())

    min_road = warshall_floyd(tizu)
    for i in range(N):
        for j in range(N):
            if tizu[i][j] > min_road[i][j]:  # 回り道をしたほうが速い。
                print(-1)
                return

    # 残っているのは、回り道をしても早くならないもののみ。
    # → 2点間距離と、別の町に行ってから目的地に行く距離とは、同じかそれより大きいかしかない。
    # → 経由地は1つだけ考えれば良い。

    for keiyu in range(N):
        for i in range(N):
            if i == keiyu: continue
            for j in range(N):
                if j == keiyu: continue
                if tizu[i][j] == tizu[i][keiyu] + tizu[keiyu][j]:
                    min_road[i][j] = 0
                    min_road[j][i] = 0
    
    ans = 0
    for i in range(N):
        ans += sum(min_road[i])

    print(ans//2)


main()