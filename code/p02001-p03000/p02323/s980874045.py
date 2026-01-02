
import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
inp = sys.stdin.buffer.readline
def inpS(): return inp().rstrip().decode()
readlines = sys.stdin.buffer.readlines
MOD = 10 ** 9 + 7
INF = 1 << 60

# ---------------------------------------------------
# ---------------------------------------------------
# ---------------------------------------------------

def resolve():
    def rec(S, v):
        if dp[S][v] >= 0:
            return dp[S][v]
        if S == (1<<V)-1 and v==0:
            dp[S][v] = 0
            return 0
        res = INF
        for to in range(V):
            if not (S>>to & 1):
                res = min(res, rec((S | (1<<to)), to) + dist[v][to])

        dp[S][v] = res
        return res

    V, E = map(int, input().split())
    dist = [[INF] * V for _ in range(V)]
    for i in range(E):
        x, y, d = map(int, input().split())
        dist[x][y] = d

    dp = [[-1] * V for _ in range(1 << V)]

    res = rec(0, 0)
    if res == INF:
        print(-1)
    else:
        print(res)

if __name__ == '__main__':
    resolve()
