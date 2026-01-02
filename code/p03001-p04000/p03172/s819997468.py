import itertools
n, k = map(int, input().split())
a = list(map(int, input().split()))
M = 10**9 + 7

dp = [[None] * (k + 1) for _ in range(n + 1)]
def dfs(i=0, at=k):
    if dp[i][at] is not None:
        return dp[i][at]

    if i == n:
        r = int(at == 0)
        dp[i][at] = r
        return r

    cnt = 0
    for v in range(a[i] + 1):
        if v > at:
            break
        cnt += dfs(i + 1, at - v)
    dp[i][at] = cnt
    return cnt
#
# print(dfs())
# for v in dp:
#     print(v)

def fm(array):
    return ["*" if v is None else v for v in array]

def mod(v):
    if v >= M:
        return v % M
    return v

# def addmod(a, b):
#     return mod(a + b)

# for at in range(k + 1):
for i in reversed(range(n + 1)):
    for at in range(k + 1):
        if i == n:
            dp[i][at] = int(at == 0)
            continue
        cnt = 0
        # print(*fm(dp[i]), end=" -> ")
        # for v in range(min(a[i], at) + 1):
        #     cnt += dp[i + 1][at - v]
        # dpcnt = cnt
        cnt = cs[at] - cs[at - min(a[i], at) - 1]
        dp[i][at] = mod(cnt)
        # print(*fm(dp[i]), "@", at - min(a[i], at), "~", at)
        # print(cnt, "@", at - min(a[i], at), "~", at, ":", *fm(dp[i + 1])[at - min(a[i], at):at + 1])
        # print(dpcnt, cnt)
    # cs = list(itertools.accumulate(dp[i], func=addmod)) + [0]
    cs = list(itertools.accumulate(dp[i])) + [0]
    cs = [mod(v) for v in cs]
    # print(*cs, "cs")
    # print(*dp[i], "dp")
    # print("-----")
print(dp[0][k] % M)

# for v in dp:
#     print(*fm(v))
