
import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))

from math import ceil

h,w = readints()

s = [readstr() for i in range(h)]

dp = [[0]*w for i in range(h)]

if s[0][0] == '.':
    dp[0][0] = 0
else:
    dp[0][0] = 1

for i in range(1,h):
    if s[i][0] != s[i-1][0]:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0] 

for i in range(1,w):
    if s[0][i] != s[0][i-1]:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1]

for i in range(1,h):
    for j in range(1,w):
        if s[i][j] != s[i-1][j]:
            dp[i][j] = dp[i-1][j] + 1
        else:
            dp[i][j] = dp[i-1][j]
        if s[i][j] != s[i][j-1]:
            dp[i][j] = min(dp[i][j-1] + 1,dp[i][j])
        else:
            dp[i][j] = min(dp[i][j-1],dp[i][j])

print(ceil(dp[-1][-1]/2))



