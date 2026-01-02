import sys;
import math;
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()

N,W = get_ints();
arr = [];
for i in range(N):
    tarr = get_array();
    arr.append(tarr);
dp = [[0 for i in range(W+1)] for i in range(N+1)];
for i in range(1,N+1):
    for j in range(1,W+1):
        if(j-arr[i-1][0])>=0:
            dp[i][j]=max(dp[i-1][j],arr[i-1][1]+dp[i-1][j-arr[i-1][0]]);
        else:
            dp[i][j]=dp[i-1][j]


print(dp[N][W]);
    
