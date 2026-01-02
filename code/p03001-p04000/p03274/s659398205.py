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

INF = float('inf')

def solve():
    n, k = MI()
    X = LI()


    ans = INF
    for i in range(n + 1 - k):
        xl = X[i]
        xr = X[i+(k-1)]

        d_l = abs(xl)
        d_r = abs(xr)
        d_d = abs(xl - xr)
        ans = min(ans, min(d_l + d_d, d_r + d_d))
    print(ans)


if __name__ == '__main__':
    solve()
