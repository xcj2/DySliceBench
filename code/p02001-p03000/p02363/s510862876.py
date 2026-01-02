import sys, heapq
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def warshall_floyd(d):
    V = len(d)
    for i in range(V):
        d[i][i] = 0
    for k in range(V):
        for i in range(V):
            for j in range(V):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

def resolve():
    V, E = LI()
    con = [[INF]*V for _ in range(V)]
    for _ in range(E):
        s, t, d = LI()
        con[s][t] = d

    ans = warshall_floyd(con)

    has_ns = [ans[i][i]<0 for i in range(V)].count(True)>0
    if has_ns:
        print('NEGATIVE CYCLE')
    else:
        for i in ans:
            print(' '.join([str(j) if j<INF else 'INF' for j in i]))

if __name__ == '__main__':
    resolve()
