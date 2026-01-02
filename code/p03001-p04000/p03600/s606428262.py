import sys, copy
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

def warshall_floyd(d):
    V = len(d)
    d = d
    for i in range(V):
        d[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def resolve():
    N = I()
    A = [LI() for _ in range(N)]

    min_cost = copy.deepcopy(A)
    min_cost = warshall_floyd(min_cost)
    ans = copy.deepcopy(min_cost)

    if A == min_cost:
        for i in range(N):
            for j in range(N):
                if i!=j:
                    for k in range(N):
                        if k!=i and k!=j:
                            if min_cost[i][j]==min_cost[i][k]+min_cost[k][j]:
                                ans[i][j] = 0
        print(sum([sum(i) for i in ans])//2)
    else:
        print(-1)

if __name__ == '__main__':
    resolve()