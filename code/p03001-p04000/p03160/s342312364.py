import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

def solve():
    n = II()
    H = LI()

    dp = [INF] * n
    dp[0] = 0
    def f(a, b):
        return abs(a - b)
    for i in range(1, n):
        dp[i] = min(dp[i-1] + f(H[i], H[i-1]), dp[i-2] + f(H[i], H[i-2]) if i >= 2 else INF)
    print(dp[i])


if __name__ == '__main__':
    solve()
