import sys
import math

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()
a_array = naa(N)

mod = 10 ** 9 + 7
ans = [-1] * (2 ** N)


def solve(n, c):
    # print(n,c)
    # print(ans)
    if ans[n] != -1:
        return ans[n]
    ans[n] = 0
    if c == N - 1:
        ans[n] = a_array[c][int(math.log2(n))]
        return ans[n]
    for i in range(N):
        if a_array[c][i] == 0 or n & (1 << i) == 0:
            continue
        ans[n] = (ans[n] + solve(n - (1 << i), c+1)) % mod
    return ans[n]


print(solve(2**N-1, 0))
