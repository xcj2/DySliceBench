import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,k = map(int,readline().split())

mod = 10**9+7

cum = [i for i in range(10**6)]
def cumsum(lst): #元のリストを保持
    res = lst[:]
    for i in range(1,len(res)):
        res[i] += res[i-1]
    return res
cum = cumsum(cum)
def cumsumdif(l,r,lst): #求めたい差のインデックスを入れる
    if l == 0:
        return lst[r]
    else:
        return lst[r] - lst[l-1]

def reydeoro(n):
    return n*(n+1)//2

ans = 0
for i in range(k,n+1):
    ans += cum[n] -cum[n-i] - cum[i-1] + 1 #+1:al自体を含むため
    ans %= mod

print((ans+1)%mod) #k = n+1のとき