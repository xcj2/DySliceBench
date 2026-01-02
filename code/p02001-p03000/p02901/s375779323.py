import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = 10**11+1
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
import fractions
from functools import reduce
def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)
def prime_decomposition(n): #素因数分解
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(int(n))
  return table

def make_divisors(n): #約数列挙
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


n,mm = m()
ke = set([i+1 for i in range(n)])
bo = [[] for i in range(n)]
dp = [Max for i in range(2**n)]
kkk = []
dp[0] = 0
waa = set()
for i in range(mm):
    a,b = m()
    c = l()
    bit = 0
    on = 0
    for i in c:
        bit |= 1 << (i-1)
    waa = waa | set(c)
    for j in range(2**n):
        dp[j|bit] = min(dp[j|bit] ,dp[j] + a)
    
kkk.sort(key = lambda x:x[1])
if ke != waa:
    print(-1)
else:
    print(dp[-1])
            


