#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def LF(): return list(map(float, input().split()))
def LC(): return [c for c in input().split()]
def LLI(n): return [LI() for _ in range(n)]
def NSTR(n): return [input() for _ in range(n)]

def array2d(N, M, initial=0):
    return [[initial]*M for _ in range(N)]

def copy2d(orig, N, M):
    ret = array2d(N, M)
    for i in range(N):
        for j in range(M):
            ret[i][j] = orig[i][j]
    return ret


INF = float("inf")
MOD = 10**9 + 7

class BIT:
    # 1-index
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


def main():
    N, Q = MAP()
    c = [None]+LI()
    lri = [(l, r, i) for i, (l, r) in enumerate(LLI(Q))]
    ans = [0]*Q

    # クエリは右端でソート
    lri.sort(key=lambda x: x[1])
    good_ball = [-1]*(N+1)
    acc = BIT(N)

    # 1-indexで統一したい
    curr = 1
    # 始めの一つの更新
    acc.add(curr, 1)
    good_ball[c[1]] = 1
    for l, r, i in lri:
        # currがrに到達するまで、良い玉の集合を更新する。
        while r > curr:
            curr += 1
            cc = c[curr]
            # 良い玉が既にあれば、bitから除く
            if good_ball[cc] != -1:
                acc.add(good_ball[cc], -1)
            acc.add(curr, 1)
            # 良い玉の位置を更新する
            good_ball[cc] = curr
        # print(l, r, curr, dict(good_ball))
        # print([acc.sum(i+1) for i in range(N)])

        # クエリに答える
        # [l, r]に対する答えはsum(r)-sum(l-1)
        ans[i] = acc.sum(r)-acc.sum(l-1)

    print(*ans, sep="\n")

    return


if __name__ == '__main__':
    main()
