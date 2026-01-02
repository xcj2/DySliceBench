import sys
sys.setrecursionlimit(100000)

def intinput(): return map(int,input().split())

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i!=0:
            t[i],t[i-1]=t[i-1],t[i]
        if "".join(t).count("AGC")>=1:
            return False
    return True

n=int(input())
mod=10**9+7
memo=[{} for i in range(n+1)]

def dfs(last3="TTT",cnt=0):
    if last3 in memo[cnt]:
        return memo[cnt][last3]
    if cnt==n:
        return 1
    ans=0
    for i in "AGCT":
        last4 = last3+i
        if ok(last4):
            ans = ans+dfs(last4[1:],cnt+1)
    memo[cnt][last3]=ans
    return ans

print(dfs()%mod)