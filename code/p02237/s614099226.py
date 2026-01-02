import sys, collections
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

def resolve():
    n = I()
    Adj = [[0]*n for _ in range(n)]
    for _ in range(n):
        ukv = LI()
        u = ukv[0]
        # k = ukv[1]
        v = ukv[2:]
        for i in v:
            Adj[u-1][i-1] = 1

    for i in Adj:
        print(*i)

if __name__ == '__main__':
    resolve()

