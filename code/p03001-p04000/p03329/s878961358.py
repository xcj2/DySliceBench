import sys
stdin = sys.stdin

sys.setrecursionlimit(10**5)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x)-1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

n = ni()

res = 1
coin = [1]
i = 1
while res < 10**5:
    coin.append(6**i)
    i += 1
    res *= 6
    
res = 1
i = 1
while res < 10**5:
    coin.append(9**i)
    i += 1
    res *= 9
    
coin.sort()
    
dp = [10**5]*(n+1)
dp[0] = 0

for i in range(1,n+1):
    for c in coin:
        if i-c >= 0:
            dp[i] = min(dp[i], dp[i-c]+1)
            
print(dp[n])