H, N = map(int, input().split())
INF = int(1e12)

def l():
    a, b = map(int, input().split())
    return P(a, b)

class P:
    def __init__(self, f, s):
        self.f = f
        self.s = s

    def __lt__(self, other):
        return self.s * other.f < other.s * self.f

AB = [l() for _ in range(N)]
AB = sorted(AB)

HMAX = H + 10000

dp = [INF] * (HMAX + 1)
dp[0] = 0
for i in range(HMAX):
    for p in AB:
        if i + p.f > HMAX:
            continue
        dp[i + p.f] = min(dp[i + p.f], dp[i] + p.s)

for i in range(HMAX - 1, -1, -1):
    dp[i] = min(dp[i + 1], dp[i])

print(dp[H])
