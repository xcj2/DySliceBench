#from fractions import gcd
from collections import Counter
mod = 10**9+7
def inv(a):
  return pow(a,mod-2,mod)
def prm(a):
  if a == 1 or a == 4:
    return False
  for i in range(2,int((a)**0.5+1)):
    if a%i == 0:
      return False
  else:
    return True
prime = []
for i in range(1,10**4+1):
  if prm(i):
    prime.append(i)
def sepa(a):
  ans = []
  while a>1:
    for x in prime:
      if a%x == 0:
        ans.append(x)
        a = a//x
        break
      elif x == prime[-1]:
        ans.append(a)
        a = 1
  return Counter(ans)
n = int(input())
a = list(map(int,input().split()))
f = [inv(a[i]) for i in range(n)]
lcm = sepa(1)
for i in range(n):
  x = sepa(a[i])
  for y,z in x.items():
    if z>lcm[y]:
      lcm[y] = z
k = 1
for i,j in lcm.items():
  k = k*(i**j)%mod
print(k*sum(f)%mod)