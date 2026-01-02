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
    s1 = SS()
    s2 = SS()

    l1 = len(s1)
    l2 = len(s2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1+1):
        dp[i][0] = i
    for i in range(l2+1):
        dp[0][i] = i

    for i in range(l1):
        for j in range(l2):
            r_cost = 0 if s1[i] == s2[j] else 1
            dp[i+1][j+1] = min(dp[i][j] + r_cost, dp[i+1][j] + 1, dp[i][j+1] + 1)

    print(dp[-1][-1])

if __name__ == '__main__':
    resolve()
