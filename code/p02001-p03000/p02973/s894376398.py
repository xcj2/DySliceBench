import sys, bisect
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

def lis_(a):
    dp = [INF]*len(a)
    for i in a:
        dp[bisect.bisect_left(dp, i+1)] = i
    return bisect.bisect_left(dp, INF)

def resolve():
    N = I()
    A = [I() for _ in range(N)]
    A = A[::-1]

    print(lis_(A))

if __name__ == '__main__':
    resolve()
