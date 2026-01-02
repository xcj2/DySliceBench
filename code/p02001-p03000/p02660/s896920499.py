def create_divisors(n):
  """
  自然数nの全ての約数を列挙したリストを作成する。

  Parameters
  ----------
  n : int
    自然数

  Returns
  -------
    divisors：list

  """
  divisors=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      divisors.append(i)
      if i!=n//i:
        divisors.append(n//i)
  divisors.sort()
  return divisors
def factorization(n):
    """
    引数の値を素因数分解したリストを返す

    Parameters
    ----------
    n : int
        素因数分解したい自然数

    Returns
    -------
    retlist : list
        2以上の整数n => [[素因数, 指数], ...]の2次元リスト
    """
    retlist = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            retlist.append([i, cnt])

    if temp!=1:
        retlist.append([temp, 1])

    if retlist==[]:
        retlist.append([n, 1])

    return retlist
def isPrime(x):
  """
  xが素数か否か判定する。

  Parameters
  ----------
  x: int
      自然数

  Returns
  -------
      True:素数
      False:素数ではない
  """
  if x<2:
    return False
  for i in range(2,int(x**0.5)+1):
    if x%i==0:
      return False
  return True

n=int(input())
d=factorization(n)

p=[]
for i in range(len(d)):
  if isPrime(d[i][0]):
    p.append(d[i]) 

# print(p)
from collections import Counter
used=Counter()
ans=0
for i in range(len(p)):
  t=p[i][1]
  j=1
  t_sum=0
  while t>0 and t>=j:
    if used[p[i][0]**j]==0:
      ans+=1
    used[p[i][0]**j]+=1
    t-=j
    j+=1
print(ans)




