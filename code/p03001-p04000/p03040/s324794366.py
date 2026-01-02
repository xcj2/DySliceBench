import sys,collections as cl,bisect as bs,heapq as hq
sys.setrecursionlimit(100000)
input = sys.stdin.readline
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
  if len(x) == 0:
    return []
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

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

"""
def nibu(x,n,r):
  ll = 0
  rr = r
  while True:
    mid = (ll+rr)//2

  if rr == mid:
    return ll
  if (ここに評価入れる):
    rr = mid
  else:
    ll = mid+1
"""

q = onem()

b = 0

AR = []
AL = []

ans = 0



for i in range(q):
  a = l()
  if len(a) == 1:
    if len(AR) == len(AL):
      print(min(AR[0]*-1,AL[0]),ans + b)
    else:
      print(AR[0]*-1,ans + b)

  else:
    b += a[2]
    if AR == []:
      AR.append(-a[1])
    else:
      if len(AR) == len(AL):
        if AL[0] < a[1]:
          ans += a[1]-AL[0]
          hq.heappush(AL,a[1])
          ppp = hq.heappop(AL)
          hq.heappush(AR,ppp*-1)
        else:
          if -1*AR[0] > a[1]:
            ans += (-1*AR[0] - a[1])
          hq.heappush(AR,a[1]*-1)

      else:
        if (AR[0]* -1) > a[1]:
          ans += (-1*AR[0] - a[1])
          hq.heappush(AR,a[1]*-1)
          ppp = hq.heappop(AR)*-1
          hq.heappush(AL,ppp)
        else:
          ans += (AR[0] + a[1])
          hq.heappush(AL,a[1])





