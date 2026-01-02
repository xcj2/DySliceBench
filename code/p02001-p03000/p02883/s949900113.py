import sys,collections as cl,bisect as bs,heapq as hq
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
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

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


def ok(x,p):
    kkk = 0
    for i in range(len(x)):
        kkk += max(0,-(-(x[i][0] - p) // x[i][2]))
    return kkk


n,k = m()
a = l()

f = l()

for i in range(n):
    a[i]


a.sort(reverse = True)

f.sort()
co = 0

d = []

for i in range(n):
    d.append([a[i]*f[i],a[i],f[i]])

d.sort(reverse = True)



ll = 0

rr = d[0][0] 


while True:
    mid = (rr+ll)//2

    if rr == mid:
        break

    if ok(d,mid) <= k:
        rr = mid
    else:
        ll = mid+1

print(ll)







