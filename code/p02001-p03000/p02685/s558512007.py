import sys
from functools import lru_cache
 
#read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
def cmb(n, r):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % mod
n,m,k=reads()
N = n-1 # N は必要分だけ用意する
mod =  998244353
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

mod=998244353
numbers=[m]
for i in range(n-1):
  numbers.append(numbers[i]*(m-1)%mod)
ans=0
for i in range(k+1):
  ans+=numbers[n-i-1]*cmb(n-1,i)
ans%=mod
#print(numbers)
print(ans)
