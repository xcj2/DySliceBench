from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = float("inf")


class CumulativeSum:
    def __init__(self, l):
        self.dp = [0] * (len(l) + 1)
        for i, v in enumerate(l):
            self.dp[i + 1] = v + self.dp[i]

    # return sum(l[left] + l[left + 1] + ... + l[right])
    def total(self, left, right):
        assert 0 <= left <= right < len(self.dp)
        return self.dp[right + 1] - self.dp[left]


def main():
    N, K = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = [max(0, a) for a in a_list]

    cs_a = CumulativeSum(a_list)
    cs_b = CumulativeSum(b_list)

    ans = -INF
    total = sum(b_list)
    for i in range(N - K + 1):
        a = max(0, cs_a.total(i, i + K - 1))
        rest = total - cs_b.total(i, i + K - 1)
        ans = max(ans, rest + a)
    print(ans)

if __name__ == '__main__':
    main()
