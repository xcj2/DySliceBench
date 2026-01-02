import numpy as np


def get_max():
    a = 0

    def _max(x):
        nonlocal a
        a = max(a, x)
        return a

    return _max


def solve(fwd, bck):
    dp = []
    cur = 0
    for x, v in fwd:
        cur -= x
        cur += v
        dp.append(cur)

    dp = list(map(get_max(), dp))

    cur = 0
    ans = dp[-1]
    for i, (x, v) in enumerate(bck[:-1]):
        cur -= 2 * x
        cur += v
        # print(i, x, v, ans, cur, dp[n - i - 2])
        ans = max(ans, dp[n - i - 2] + cur)
        # print(i, x, v, ans, cur, dp[n - i - 2])

    return ans


n, c = map(int, input().split())
sushi = [list(map(int, input().split())) for _ in range(n)]

fwd = np.array(sushi).T
fwd[0] = np.diff(np.concatenate(([0], fwd[0])))
fwd = fwd.T.tolist()

bck = np.array(sushi).T
bck[0] = np.diff(np.concatenate(([0], (c - bck[0])[::-1])))
bck[1] = bck[1][::-1]
bck = bck.T.tolist()

# print(fwd)
# print(bck)

print(max(solve(fwd, bck), solve(bck, fwd)))
