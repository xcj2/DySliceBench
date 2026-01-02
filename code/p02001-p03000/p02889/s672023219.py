import sys

sys.setrecursionlimit(10 ** 7)
# debug = True

debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

def matdprint(mat):
    if debug == True:
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                print(mat[i][j], end=', ')
            print()

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()

INF = 10 ** 18
MOD = 10 ** 9 + 7
def conv(s):
    cnt = 0
    for n in s:
        cnt += 2**n
    return cnt

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d


def nr_warshall_floyd(nr, d, L):
    #nr[i][j]: (iからjへの最短補給回数, iからjへ最短補給回数でやった時の残り燃料)
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # そもそもkルートが可能か判断
                if d[i][k] == INF:
                    continue
                if d[k][j] == INF:
                    continue

                # kで補給がいるかの判断
                num_at_k = nr[i][k][0]
                res_at_k = nr[i][k][1]

                num_at_j = num_at_k + nr[k][j][0]
                res_at_j = res_at_k - d[k][j]
                if d[k][j] > res_at_k:
                    # 補給が必要。補給してすすむ
                    num_at_j += 1
                    res_at_j = L - d[k][j]
                else:
                    # 補給がいらない
                    pass

                if num_at_j < nr[i][j][0]:
                    # 採用
                    nr[i][j] = (num_at_j, res_at_j)
                elif num_at_j > nr[i][j][0]:
                    # 不採用
                    pass
                else:
                    # 等しいときは残り燃料で比べる
                    nr[i][j] = (num_at_j, min(nr[i][j][1], res_at_j))
    return nr

def main():

    N, M, L = LI()
    abc_list = []
    for i in range(M):
        a, b, c = LI()
        abc_list.append((a-1,b-1,c)) # 0 origin

    q_list = []
    Q = II()
    for i in range(Q):
        s, t = LI()
        q_list.append((s-1, t-1)) # 0 origin

    # ワーシャルフロイドもどきをやる
    dmx = INF
    nmx = N+1
    d = [[dmx for i in range(N)] for i in range(N)]
    nr = [[(nmx, 0) for i in range(N)] for i in range(N)]

    # 初期化
    for i in range(N):
        d[i][i] = 0
        nr[i][i] = (0, L)

    for a, b, c in abc_list:
        if c > L:
            # そもそも燃料が足りず通れないことがある
            pass
        else:
            d[a][b] = c
            d[b][a] = c

            nr[a][b] = (0, L-c)
            nr[b][a] = (0, L-c)

    # 最短経路
    d = warshall_floyd(d)
    # 回数
    # nr = nr_warshall_floyd(nr, d, L)
    # dprint(d)
    # dprint(nr)
    # for s, t in q_list:
    #     ans = nr[s][t][0]
    #     if ans == nmx:
    #         print(-1)
    #     else:
    #         print(ans)

    n = [[nmx for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if d[i][j] <= L:
                n[i][j] = 1

    n = warshall_floyd(n)

    for s, t in q_list:
        ans = n[s][t]
        if ans == nmx:
            print(-1)
        else:
            print(ans - 1)


main()