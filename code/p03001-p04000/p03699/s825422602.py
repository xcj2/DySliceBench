import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    nums = [0]
    for _ in range(n):
        nums.append(I())
    
    dp = [[False]*(10001) for _ in range(n+1)]
    dp[0][0] = True
    ans = 0
    for i in range(1,n+1):
        num = nums[i]
        for j in range(10000):
            if num > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
            if dp[i][j] and j%10 != 0:
                ans = max(ans,j)
    print(ans)


main()            
