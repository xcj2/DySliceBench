import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

## DFS

def main():

    #入力受け取り
    N, Q = mi()
    x = li2(N-1)

    cnt = [0]*N
    for i in range(Q):
        p0, p1 = mi()
        cnt[p0-1] += p1

    #隣接リスト作成
    adj = [[] for i in range(N)]
    for i in range(N-1):
        #x[i][0] -= 1
        #x[i][1] -= 1
        adj[x[i][0]-1].append(x[i][1]-1)
        adj[x[i][1]-1].append(x[i][0]-1)

    #DFS
    global ans
    ans = [0]*N

    def dfs(fr, nx):
        ans[nx] += ans[fr] + cnt[nx]
        for v in adj[nx]:
            if v != fr:
                dfs(nx, v)

    dfs(0, 0)
    '''
    for i in range(N):
        print(ans[i], '', end='')
    '''
    print(*ans)

if __name__ == "__main__":
    main()