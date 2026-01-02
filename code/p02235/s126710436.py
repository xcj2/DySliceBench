from collections import defaultdict
from bisect import bisect_left, bisect, insort_left, insort
INF = 10000
def lcs(s1, s2):
    c = defaultdict(list)
    for i, s in enumerate(s1):
        c[s].append(i)
    for s in set(s2):
        c[s].append(INF)
    def g(li, a):
        for i in li:
            if i >= a:
                return i
        return -1
    dp = []
    for s2_k in s2:
        bgn_idx = 0
        for i, cur_idx in enumerate(dp):
            chr_idx = c[s2_k][bisect_left(c[s2_k], bgn_idx)]
            if chr_idx == INF:
                break
            dp[i] = min(cur_idx, chr_idx + 1)
            bgn_idx = cur_idx
        else:
            chr_idx = c[s2_k][bisect_left(c[s2_k], bgn_idx)]
            if chr_idx != INF:
                dp.append(chr_idx + 1)
    return len(dp)
def solve():
    N = int(input())
    for _ in range(N):
        x = input()
        y = input()
        print(lcs(x, y))
solve()

