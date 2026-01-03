import bisect
from itertools import accumulate
# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def solve():
    N, K = map(int, input().split())
    L = [int(input()) for _ in range(N)]

    L_acc = [0]+list(accumulate(L))
    for i in range(N+1):
        L_acc[i] -= (i)*K

    L_sort = list(sorted(set(L_acc)))
    L_comp = [-1]*(N+1)
    for i in range(N+1):
        key = L_acc[i]
        ind = bisect.bisect_left(L_sort, key)
        L_comp[i] = ind
    # BIT
    bit = [0]*(N+1)

    def sum_bit(i):
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & (-i)
        return s

    def add(i, x):
        while i <= N:
            bit[i] += x
            i += i & (-i)

    ans = 0
    for i, l in enumerate(L_comp):
        if l == 0:
            ans += N-i
            continue
        ans += sum_bit(l)
        add(l, 1)
    print(ans)


solve()
