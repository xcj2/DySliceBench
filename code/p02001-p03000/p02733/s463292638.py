import sys
from collections import defaultdict, deque, Counter
import math

# import copy
from bisect import bisect_left, bisect_right
import heapq

# sys.setrecursionlimit(1000000)

# input aliases
input = sys.stdin.readline

getS = lambda: input().strip()
getN = lambda: int(input())
getList = lambda: list(map(int, input().split()))
getZList = lambda: [int(x) - 1 for x in input().split()]

INF = 10 ** 20
MOD = 10**9 + 7
divide = lambda x: pow(x, MOD-2, MOD)


def nck(n, k, kaijyo):
    return (npk(n, k, kaijyo) * divide(kaijyo[k])) % MOD


def npk(n, k, kaijyo):
    if k == 0 or k == n:
        return n % MOD
    return (kaijyo[n] * divide(kaijyo[n-k])) % MOD


def kaijyo(n):
    ret = [1]
    for i in range(1, n + 1):
        ret.append((ret[-1] * i)% MOD)
    return ret


def cut(pt, grid, k, h, w):
    pat = []
    for i in range(h-1):
        if pt % 2 == 1:
            pat.append("1")
        else:
            pat.append("0")
        pt //= 2

    # print("pat", pat)
    slice = Counter(pat)["1"]
    pat = pat + ["0"]
    white = [0] * (slice + 1)
    ret = 0
    for i in range(w):
        tw = [0] * (slice + 1)
        dan = 0
        for j in range(h):
            if grid[j][i] == "1":
                tw[dan] += 1
            if pat[j] == "1":
                dan += 1

        if max(tw) > k:
            return INF
        reset = False
        for w1, w2 in zip(white, tw):
            if w1 + w2 > k:
                ret += 1
                reset = True
                break
        if reset:
            white = tw
        else:
            for up in range(slice + 1):
                white[up] += tw[up]

    return ret + slice

def solve():
    h, w, k = getList()
    grid = []
    for i in range(h):
        grid.append(getS())

    ans = INF
    for i in range(2 ** (h-1)):
        tmp = cut(i, grid, k, h, w)
        # print(tmp)
        ans = min(ans, tmp)
    print(ans)


def main():
    n = getN()
    for _ in range(n):
        solve()


if __name__ == "__main__":
    # main()
    solve()