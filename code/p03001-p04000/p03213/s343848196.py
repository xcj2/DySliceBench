import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Factoring by trial split
def getPrimeList(n):
  l=[]
  t=int(math.sqrt(n))+1
  
  for a in range(2,t):
    while n%a==0:
      n//=a
      l.append(a)
  
  if n!=1:
    l.append(n)
  
  return l

# Summarize count of factor within list
def summarize_list(l):
  sl=sorted(l)

  a=sl[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append([a,c])
      a=x
      c=1
  res.append([a,c])

  return res

# nCr
def nCr(n,r):
  if n<r:
    return 0
  return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

# 方針
# 素因数が74個同じ数をもつ数字は七五数になる
# 素因数が24個同じ数をもち、2個同じ数を持つ数字も七五数になる
# …
# 素因数が4個同じ数をもち、4個同じ数を持ち、2個同じ数を持つ数字も七五数になる
# n!を素因数分解して上記を何パターン作れるか考える

# 手順
# n!を素因数分解する
# 74個もち・24個もち・14個持ち・4個持ち・2個もちに分類
# 上記で挙げたパターンを全て数え上げて足す

# 注意
# 例えば、24個持ち・2個持ちを取る場合
# 24個持ちから取った数字は2個持ちと重複できないので引いておくこと
# また、2個持ちなどは引数が2個のものからだけでなく
# それ以上の個数を持つものからも取れる
# つまり、24個持ちも14個持ち・4個持ち・2個持ちとして扱える

# n=1 のときはバグるので return 0 するようにした
# 最大・最小パターンはチェックする癖をつけたい

def main():
  n=I()

  if n==1:
    return 0

  l1=[]
  for i in range(2,n+1):
    l1+=getPrimeList(i)

  l1=summarize_list(l1)

  l1=sorted(l1,key=lambda x:x[1],reverse=True)

  # print(l1)

  # print(l)

  ans=[]

  # 75・25・15・5・3
  l2=[0]*5
  for x in l1:
    if x[1]>=74:
      l2[0]+=1
    elif x[1]>=24:
      l2[1]+=1
    elif x[1]>=14:
      l2[2]+=1
    elif x[1]>=4:
      l2[3]+=1
    elif x[1]>=2:
      l2[4]+=1

  # print(l2)

  # 75
  ans.append(l2[0])

  # 25・3
  ans.append(sum(l2[:2])*(sum(l2[:5])-1))

  # 15・5
  ans.append(sum(l2[:3])*(sum(l2[:4])-1))

  # 5・5・3
  ans.append(nCr(sum(l2[:4]),2)*(sum(l2[:5])-2))

  return sum(ans)

# main()
print(main())
