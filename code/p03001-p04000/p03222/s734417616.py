H, W, K = map(int, input().split())
MOD = 10**9 + 7

dp = [[0] * (W + 2) for _ in range(H + 1)]  # dp[h][w] = 上からh本通った後にwにいるパターン数
dp[0][1] = 1

preCnt = [0] * (W + 1)  # w本を任意に引けるときの数
for w in range(1, W + 1):
    cnt = 0
    for bit in range(1 << w):
        if bin(bit).count('11') == 0:
            cnt += 1
    preCnt[w] = cnt

def left(w):
    ret = 1
    ret *= preCnt[w - 3] if w - 3 > 0 else 1
    ret *= preCnt[W - w - 1] if W - w - 1 > 0 else 1
    return ret % MOD

def right(w):
    ret = 1
    ret *= preCnt[w - 2] if w - 2 > 0 else 1
    ret *= preCnt[W - w - 2] if W - w - 2 > 0 else 1
    return ret % MOD

def mid(w):
    ret = 1
    ret *= preCnt[w - 2] if w - 2 > 0 else 1
    ret *= preCnt[W - w - 1] if W - w - 1 > 0 else 1
    return ret % MOD

for h in range(1, H + 1):
    for w in range(1, W + 1):
        dp[h][w] += dp[h - 1][w - 1] * left(w)
        dp[h][w] += dp[h - 1][w] * mid(w)
        dp[h][w] += dp[h - 1][w + 1] * right(w)
        dp[h][w] %= MOD

print(dp[H][K])