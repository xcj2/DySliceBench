import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7

N, A = MI()
X = LMI()

# dp[i][j][s] := i番目までのカードからj枚を選んで合計がsになる組み合わせの数
dp = [[[0] * 2502 for _ in range(N + 2)] for _ in range(N + 1)]
for i in range(N):
    dp[i][0][0] = 1
dp[0][1][X[0]] = 1
for i in range(1, N):
    for j in range(1, i + 2):
        for s in range(A * N + 1):
            if s - X[i] < 0:
                dp[i][j][s] = dp[i - 1][j][s]
            else:
                dp[i][j][s] = dp[i - 1][j][s] + dp[i - 1][j - 1][s - X[i]]

ans = 0
for i in range(1, N + 1):
    ans += dp[N - 1][i][A * i]
print(ans)
