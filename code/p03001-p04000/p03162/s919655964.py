def solve(N, happiness):
  dp = [[0 for _ in range(3)] for _ in range(N)]
  dp[0][0] = happiness[0][0]
  dp[0][1] = happiness[0][1]
  dp[0][2] = happiness[0][2]

  for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + happiness[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + happiness[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + happiness[i][2]

  print(max(dp[N-1]))

def iin(): return int(input())
def iln(): return list(map(int, input().split()))

N = iin()
happiness = []
for i in range(N):
  happiness.append(iln())
solve(N, happiness)