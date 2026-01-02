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

def warshall_floyd(d):
    V = len(d)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def resolve():
    H, W = LI()
    c = [LI() for _ in range(10)]
    A = [LI() for _ in range(H)]

    min_cost = warshall_floyd(c)
    # for i in min_cost:
    #     print(i)
    ans = 0
    for i in A:
        for j in i:
            if 0<=j<=9:
                ans += min_cost[j][1]
    print(ans)

if __name__ == '__main__':
    resolve()