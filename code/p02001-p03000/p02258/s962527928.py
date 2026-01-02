import sys
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
    R = [I() for _ in range(n)]

    ans = -INF
    min_v = INF
    for i in range(n):
        ans = max(R[i]-min_v, ans)
        min_v = min(R[i], min_v)

    print(ans)

if __name__ == '__main__':
    resolve()
