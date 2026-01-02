# @author 

import sys

class QFlowers:
    def solve(self):
        n = int(input())
        h = [int(_) for _ in input().split()]
        a = [int(_) for _ in input().split()]

        # h = [(h[i], i) for i in range(n)]
        # h.sort()

        def update(i, x):
            while i < n + 1:
                if x > dp[i]:
                    dp[i] = x
                i += i & -i

        def get(i):
            mx = 0
            while i > 0:
                if dp[i] > mx:
                    mx = dp[i]
                i -= i & -i
            return mx

        dp = [0] * (n + 1)
        for i, he in enumerate(h):
            update(he, get(he - 1) + a[i])

        # print(dp)
        print(max(dp))

solver = QFlowers()
input = sys.stdin.readline

solver.solve()
