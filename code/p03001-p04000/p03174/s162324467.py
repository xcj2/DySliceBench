import sys
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = [IL() for _ in range(N)]

dp = [0]*(1 << N)
for i in range(N):
  dp[1 << i] = a[0][i]
#print(dp)

for i in range(2, N+1): # 1が立っている数
  n = (1 << i) - 1
  while n < (1 << N):
    x = n
    
    for j in range(N):
      if (x >> j) & 1:
        if a[i - 1][j] == 1:
          dp[x] += dp[x ^ (1 << j)] %mod

    """
    while x != 0:
      if x & 1 == 1:
        if a[i - 1][cnt] == 1:
          DP[n] = (DP[n] + DP[n & ~(1 << (cnt))]) % MOD
      x >>= 1
      cnt += 1
    """
    
    x = n & -n
    y = n + x
    n = ((n & ~y) // x >> 1) | y

print(dp[-1] %mod)