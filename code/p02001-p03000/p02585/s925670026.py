#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
from bisect import bisect_left
from itertools import product
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


def main():
    N, K = MAP()
    P = LI_()
    C = LI()

    # サイクルとは閉路のことである。順列の性質として、有向グラフで記述した時、必
    # ずサイクルの集合となる。
    ans = -INF
    for i in range(N):
        v = i
        cycle_sum = 0
        cycle_cnt = 0

        # iを始点とし、閉路の和と長さを求める
        while True:
            cycle_cnt += 1
            cycle_sum += C[v]
            v = P[v]
            if v == i:
                break

        path = 0
        cnt = 0

        while True:
            cnt += 1
            path += C[v]
            if cnt > K:
                break

            # サイクルを可能な限りまわる。サイクルの総和が負の場合は回らない
            num = (K-cnt)//cycle_cnt
            score = path + max(0, cycle_sum)*num
            ans = max(ans, score)

            v = P[v]
            if v == i:
                break

    print(ans)
    return


if __name__ == '__main__':
    main()
