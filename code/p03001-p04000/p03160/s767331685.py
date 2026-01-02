from collections import defaultdict 
import sys
import math 
import random
def get_array(): return list(map(int , sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()

sys.setrecursionlimit(10**5)

def r(ind):
    if dp[ind]!=-1:
        return dp[ind]
    if ind+1>=n:
        return 0
    ans1 = abs(a[ind+1]-a[ind])+r(ind+1)
    if ind+2>=n:
        dp[ind] = ans1 
        return dp[ind] 
    ans2 = abs(a[ind+2]-a[ind])+r(ind+2)
    dp[ind] = min(ans1,ans2)
    return dp[ind]

n = int(input())
a = get_array()
dp = [-1]*(n+5) 
print(r(0))
