def solve(N, probs):
  # dp[i][j]: probability of having j heads in i coin tosses
  # shorter version: dp[j]: probability of j heads
  dp = [0 for _ in range(N + 1)]
  dp[0] = 1

  for toss_id in range(1, N + 1):
    head_prob = probs[toss_id - 1]
    tail_prob = 1.0 - probs[toss_id - 1]
    # only until i needed
    for j in range(toss_id, -1, -1):
      # zero heads
      if j == 0:
        dp[j] = dp[j] * tail_prob
      else:
        dp[j] = (dp[j] * tail_prob) + (dp[j - 1] * head_prob)

  # sum all probabilies where heads > tails
  ans = sum(dp[N // 2 + 1:])
  print(ans)


def iin(): return int(input())
def fln(): return list(map(float, input().split()))


N = iin()
probs = fln()
solve(N, probs)
