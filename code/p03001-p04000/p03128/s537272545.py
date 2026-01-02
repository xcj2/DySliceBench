def get_int(): return int(input())
def get_float(): return float(input())
def get_line(): return input().split()
def get_lines(v): return [get_line() for _ in range(v)]
def get_int_line(): return list(map(int, get_line()))
def get_int_lines(v): return [get_int_line() for _ in range(v)]
def get_float_line(): return list(map(float, get_line()))
def get_float_lines(v): return [get_float_line() for _ in range(v)]

cost = [0,2,5,5,4,5,6,3,7,6]
N, M = get_int_line()
A = get_int_line()

dp = [-1 for _ in range(N + 1)]
dp[0] = 0
for i in range(N):
  if (dp[i] == -1): continue
  for v in A:
    if (i + cost[v] <= N and dp[i + cost[v]] < dp[i] * 10 + v):
      dp[i + cost[v]] = dp[i] * 10 + v

print(dp[N])