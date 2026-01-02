import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = int(0)

N = I()
dp = [{} for i in range(N+4)]

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]
        if ''.join(t).find('AGC') != -1:
            return False
    return True

def dfs(i, last3):
    if last3 in dp[i]:
        return dp[i][last3]
    if i == N:
        return 1
    cou = int(0)
    for s in "ACGT":
        if ok(last3+s):
            cou = (cou + dfs(i+1, last3[1:]+s)) % mod

    dp[i][last3] = cou
    return cou

ans = dfs(0,"TTT")
print(ans)
