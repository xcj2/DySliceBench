N, W = map(int, input().split())
ws, vs = zip(*[map(int, input().split()) for _ in range(N)])

def maxvalue_recursive(N, W):
    def memoize(func):
        func.d = d = {}
        def _f(*va):
            if va not in d: d[va] = func(*va)
            return d[va]
        return _f

    @memoize
    def maxvalue(i, w):
        if i < 0: return 0
        if w < ws[i]:
            return maxvalue(i - 1, w)
        else:
            return max(maxvalue(i - 1, w), maxvalue(i - 1, w - ws[i]) + vs[i])

    res = maxvalue(N - 1, W)
    return res

def maxvalue_dp(N, W, ws, vs):
    import numpy as np
    dp = np.zeros(W + 1, 'int64')
    ws = np.array(ws, 'int64')
    vs = np.array(vs, 'int64')
    for i in range(N):
        idx = np.arange(W + 1) - ws[i]
        dp = np.maximum(dp, (dp[idx] + vs[i]) * (idx >= 0))
    return dp[-1]

#print(maxvalue_recursive(N, W))
print(maxvalue_dp(N, W, ws, vs))

#import timeit
#print(timeit.timeit('maxvalue_recursive(N, W)', globals=globals(), number=10000))
#print(timeit.timeit('maxvalue_dp(N, W)', globals=globals(), number=10000))