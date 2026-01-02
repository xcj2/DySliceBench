import itertools
import os
import sys

from functools import lru_cache

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7
# MOD = 998244353


M = int(sys.stdin.buffer.readline())
DC = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]


def test(n):
    round = {str(n)}
    ret = 0
    while round:
        next_round = set()
        for n in round:
            for i in range(len(n) - 1):
                s = n[:i] + str(int(n[i]) + int(n[i + 1])) + n[i + 2:]
                if len(s) > 1:
                    next_round.add(s)
        round = next_round
        print(round)
        ret += 1
    print('test:', ret)
    print()


@lru_cache(maxsize=None)
def solve(n):
    n = str(n)
    if len(n) == 1:
        return 0, int(n)
    num = 0
    ret = 0
    for c in str(n):
        ret += 1
        num += int(c)
        while num >= 10:
            ret += 1
            num = num % 10 + 1
    return ret - 1, num


# ans = 0
# num = 0
# for d, c in DC:
#     if d == 0:
#         ans += c
#         n = num + d * c
#         ans += n // 10
#         num = n % 10
#     if d == 1:
#         ans += c
#         n = num + d * c
#         ans += n // 10
#         num = n % 10
#     if d == 2:
#         ans += c
#         n1 = c // 5
#
#         n
#         n = num + d * c
#         ans += c
#         ans += n // 10
#         num = n % 10

memo = [[None] * 11 for _ in range(10)]
for i, j in itertools.product(range(10), range(11)):
    memo[i][j] = solve(str(i) * j)


def kurikaesi(d, c):
    if c < 10:
        return memo[d][c]
    cnt, n1 = memo[d][10]
    ret = cnt * (c // 10)
    c2, n2 = kurikaesi(n1, c // 10)
    c3, n3 = memo[d][c % 10]
    ret += c2
    ret += c3
    c4, n4 = solve(str(n2) + str(n3))
    ret += c4
    return ret, n4


#
# n = ''
# for d, c in DC:
#     n += str(d) * c
# test(n)
# print(solve(n))

ans = 0
num = 0
for d, c in DC:
    cnt, n = kurikaesi(d, c)
    ans += cnt
    c2, n2 = solve(str(num) + str(n))
    ans += c2
    num = n2
print(ans - 1)
