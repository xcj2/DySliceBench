import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main_old(): 
    N, M, queries = LI()
    L = []
    R = []
    for _ in range(M):
        l, r = LI()
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for _ in range(queries):
        p, q = LI()
        P.append(p)
        Q.append(q)

    regions = [[] for _ in range(N+1)]
    for l, r in zip(L, R):
        regions[l].append(r-l)
    regions_cumsum = [[0]*(N+1) for _ in range(N+1)]
    for i in range(len(regions)):  # [0,1,1,1,2,2] みたいなのを [1, 4, 6] と変換したい。
        # まずはカウントする
        cnt = [0]*(N+1)
        for j in range(N+1):
            cnt[regions[i][j]] += 1
        # 続いて累積和を取る。
        regions_cumsum[0] = cnt[0]
        for j in range(1, N+1):
            regions_cumsum[j] = regions_cumsum[j-1] + cnt[j]

    from bisect import bisect_right
    
    for p, q in zip(P, Q):
        counter = 0
        length = q-p
        print(regions_cumsum[q] - regions_cumsum[p])




    # 駅番号: [そこから出る区間の長さのリスト] を持つ。
    # クエリを駅番号・長さに持ち替えてソート。
    # クエリごとに、駅番号において長さよりも短い電車が何本あるか見ていく。となりの駅に写ったら1引く。
    # これでQ*N？



def main(): 
    N, M, queries = LI()
    L = []
    R = []
    for _ in range(M):
        l, r = LI()
        L.append(l)
        R.append(r)
    P = []
    Q = []
    for _ in range(queries):
        p, q = LI()
        P.append(p)
        Q.append(q)

    trains = [[0]*(N+1) for _ in range(N+1)]
    for l, r in zip(L,R):
        trains[l][r] += 1

    cumsum = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            cumsum[i][j] = cumsum[i][j-1] + trains[i][j]

    for p, q in zip(P, Q):
        range_sum = 0
        for i in range(p, q+1):
            range_sum += cumsum[i][q] - cumsum[i][p-1]
        print(range_sum)

main()