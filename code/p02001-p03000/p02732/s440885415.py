from collections import Counter
from operator import mul
from functools import reduce


def inpl():
    return list(map(int, input().split()))


# 重複組み合わせは nHr = (n + r - 1)Cn
def cmb(n, r):
    # combination
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def solve(v):
    if v < 2:
        return ans
    return ans - cmb(v, 2) + cmb(v - 1, 2)


N = int(input())
A = inpl()
cA = Counter(A)

ans = 0
for v in cA.values():
    ans += v * (v - 1) // 2
# print(ans)
for a in A:
    print(solve(cA[a]))
