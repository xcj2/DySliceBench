import sys
sys.setrecursionlimit(10**9)
mod = 10**9+7
from collections import defaultdict
class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

memo = [-1]*5001
memo[0] = 1
def fact(n):
    if memo[n] != -1:
        return memo[n]
    else:
        res = n*fact(n-1)%mod
        memo[n] = res
        return res

N = int(input())
P = list(map(int,input().split()))
K = 0
u = UnionFind(N)
loop = 0
for i in range(N):
    if P[i]==-1:
        K += 1
        continue
    if u.find(i)==u.find(P[i]-1):
        loop += 1
    u.union(i,P[i]-1)

d = defaultdict(lambda:[0,0])
for i in range(N):
    if P[i]==-1:
        d[u.find(i)][0] += 1
    d[u.find(i)][1] += 1

n = []
for k in d:
    n.append(d[k])

dp = [[0]*(len(n)+1) for i in range(len(n))]
for i in range(len(n)):
    dp[i][0] = 1
for i in range(len(n)):
    for j in range(1,i+2):
        if j != i+1:
            dp[i][j] += dp[i-1][j]
        dp[i][j] += dp[i-1][j-1]*n[i][0]*n[i][1]
        dp[i][j] %= mod

ans = 0
for i in range(2,len(n)+1):
    if K-i<0:
        break
    ans += dp[len(n)-1][i]*fact(i-1)*pow(N-1,K-i,mod)
    ans %= mod
for i in range(len(n)):
    if K==0:
        break
    ans += n[i][0]*(n[i][1]-1)*pow(N-1,K-1,mod)
    ans %= mod

ans = pow(N-1,K,mod)*(N-loop)-ans
ans %= mod
print(ans)