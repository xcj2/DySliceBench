import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N, M, Q = map(int, input().split())
    LR = [LI_() for _ in range(M)]
    pq = [LI_() for _ in range(Q)]

    cnt = [[0]*N for _ in range(N)]
    for i in LR:
        cnt[i[0]][i[1]] += 1

    acc = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        for j in range(N):
            acc[i+1][j+1] = acc[i+1][j] + cnt[i][j]
    for i in range(N):
        for j in range(N):
            acc[i+1][j+1] += acc[i][j+1]

    for i in pq:
        p = i[0]
        q = i[1]
        ans = acc[q+1][q+1] - acc[p][q+1] - acc[q+1][p] + acc[p][p]
        print(ans)

if __name__ == '__main__':
    resolve()
