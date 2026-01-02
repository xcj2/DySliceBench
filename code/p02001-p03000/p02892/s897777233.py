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

debug = True
debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

def solve():
    N = II()
    edge_list = {}
    # i, j は 0 origin で入れる
    for i in range(N):
        edge_list[i] = []
        ei = SI()
        for j, e in enumerate(ei):
            if e == '1':
                edge_list[i].append(j)

    # 二部グラフチェック
    # -1, 1 をアサインしていく
    bip = [0 for i in range(N)]

    # キュー
    from collections import deque
    qu = deque()
    qu.append((-1, 0)) # 親のbip, nodeid。0はおやを-1と仮定する

    # 既読
    seen = set()
    is_bip = True


    while qu:
        parent_bip, n = qu.popleft()

        # 親と同じ側にアサインされているなら、bipではないので終了
        if parent_bip * bip[n] == 1:
            is_bip = False
            print(-1)
            return

        # 親と反対側にアサイン
        bip[n] = parent_bip * -1

        if n not in seen:
            for neib in edge_list[n]:
                qu.append((bip[n], neib))
        dprint('parent_bip:',parent_bip, 'n:', n, 'edge:', edge_list[n], 'q:', qu, seen)
        seen.add(n)

    dprint(bip)

    # bipなら直径
    mx = N + 1
    d = [[mx for i in range(N)] for i in range(N)]
    for i in range(N):
        for e in edge_list[i]:
            d[i][e] = 1
        d[i][i] = 0
    d = warshall_floyd(d)

    ans = 0
    for i in range(N):
        for j in range(N):
            ans = max(ans, d[i][j])

    dprint(d)

    print(ans+1)

solve()