import sys
sys.setrecursionlimit(10**7)

readline = sys.stdin.buffer.readline
def readstr():return readline().rstrip().decode()
def readstrs():return list(readline().decode().split())
def readint():return int(readline())
def readints():return list(map(int,readline().split()))
def printrows(x):print('\n'.join(map(str,x)))
def printline(x):print(' '.join(map(str,x)))


r,c,k = readints()
a = [[0]*(c+1) for i in range(r+1)]

for i in range(k):
    R,C,V = readints()
    a[R][C] = V

dp = [0]*(r+1)*(c+1)*4

for x in range((r+1)*(c+1)*4):
    i = x//((c+1)*4)
    l = x%((c+1)*4)
    j = l//4
    l %= 4
    if i==0 or j==0:
        continue
    if l==0:
        dp[x] = max(dp[i*(c+1)*4 + (j-1)*4], dp[(i-1)*(c+1)*4 + j*4 + 3])
    else:
        dp[x] = max(dp[i*(c+1)*4 + (j-1)*4 + l], dp[(i-1)*(c+1)*4 + j*4 + 3]+a[i][j], dp[i*(c+1)*4 + (j-1)*4 + l-1]+a[i][j])

print(dp[-1])