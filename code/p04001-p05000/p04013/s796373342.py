import sys
import numpy as np
def sinput(): return sys.stdin.readline()
def iinput(): return int(sinput())
def imap(): return map(int, sinput().split())
def fmap(): return map(float, sinput().split())
def iarr(): return list(imap())
def farr(): return list(fmap())
def sarr(): return sinput().split()

n, a = imap()
x = np.array(iarr()) - a
MAX = 50*50+1

dp = np.zeros((n+1, 2*MAX+1)).astype(int)
dp[0][MAX] = 1
for i in range(n):
    for j in range(2*MAX):
        if j-x[i] < 0 or j-x[i] > 2*MAX:
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j] + dp[i][j-x[i]]
print(dp[n][MAX]-1)
