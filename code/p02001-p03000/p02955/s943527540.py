import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize
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

    divisors.sort()
    return divisors



n,k = m()

a = l()

p = sum(a)

d = make_divisors(p)

ans = 0

for i in d:
    kkk = [0] * n
    for j in range(n):
        kkk[j] = a[j] % i
    kkk.sort()
    kkkk = sum(kkk)
    nw = 0
    for j in range(n):
        nw += kkk[j]
        nn = kkkk - nw
        if nw <= k and (n-j-1)*i - nn <= k and nw == (n-j-1)*i - nn:
            ans = i
            break
print(ans)

