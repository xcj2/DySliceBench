N = int(input())

def concat(li):
  return ''.join([str(l) for l in li])

import itertools
def init_dp(n):
  dp = {}
  for s in itertools.product(['A', 'G', 'C', 'T'],['A', 'G', 'C', 'T'],['A', 'G', 'C', 'T']):
    st = concat(s)
    if check3(st) == 0:
        dp[st] = n
  return dp

def check3(s):
  s1 = s
  s2 = s[0] + s[2] + s[1]
  s3 = s[1] + s[0] + s[2]
  if 'AGC' in '_'.join([s1, s2, s3]):
  	return 1
  return 0

def check4(s):
  s1 = s
  s2 = s[1] + s[0] + s[2] + s[3]
  s3 = s[0] + s[2] + s[1] + s[3]
  s4 = s[0] + s[1] + s[3] + s[2]
  if 'AGC' in '_'.join([s1, s2, s3, s4]):
  	return 1
  return 0
  
def update_dp(dp, next_dp, k, s):
  next4 = k + s  
  if check4(next4) == 0:
	  next_dp[next4[1:]] += dp[k]
  return next_dp

dp = init_dp(1)
for i in range(3, N):
  next_dp = init_dp(0)
  for k in dp.keys():
    for s in ['A', 'G', 'C', 'T']:
      next_dp = update_dp(dp, next_dp, k, s)
  dp = next_dp.copy()

mx = 10**9 + 7
ans = 0
for k in dp.keys():
  ans += dp[k] 
  ans %= mx
print(ans)