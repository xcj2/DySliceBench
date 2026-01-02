import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


def warsharll_floyd(c):
    n = len(c)
    for k in range(n):  # iからjへ向かう途中に中継する頂点
        for i in range(n):  # 始点
            for j in range(n):  # 終点
                # 現時点のiからjへ向かうコスト と kを経由してjに向かうコストの小さい方
                c[i][j] = min(c[i][j], c[i][k] + c[k][j])
    return c


def main():
    h, w = LI()
    c = LIR(10)
    a = LIR(h)
    # a[i][j]を1に変える最小コストを考える
    # costs[i] : i を 1 に変えるコスト
    costs = warsharll_floyd(c)
    ans = 0
    for i in range(h):
        for j in range(w):
            if a[i][j] in {-1, 1}:
                continue
            else:
                ans += costs[a[i][j]][1]
    print(ans)


main()
