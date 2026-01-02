import sys
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value

## BFS
from collections import deque

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
        x[i][0] -= 1
        x[i][1] -= 1
        adj[x[i][0]].append(x[i][1])
        adj[x[i][1]].append(x[i][0])

    que = deque()
    ans = [0]*N

    # BFS
    que.append((0, 0))
    num = 0
    while que!=deque():
        v = que.popleft()
        ans[v[1]] = ans[v[0]] + cnt[v[1]]
        for next in adj[v[1]]:
            if next != v[0]:
                que.append((v[1], next))

    for k in ans:
        print(k, '', end='')

if __name__ == "__main__":
    main()