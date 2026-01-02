import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8')
inf = float('inf') ;mod = 10**9+7
mans = inf ;ans = 1 ;count = 0 ;pro = 1
def gcd(a, b):
    while(b != 0):
        a, b = b, a % b
    return a
    
def lcm(m,n):
    return (m*n)//gcd(m,n)

n = int(input())
def make_key0(a,b):
  if a == 0 and b != 0:
    return(0,1)
  elif a != 0 and b == 0:
    return(1,0)
  if (a < 0 and b > 0) or (a > 0 and b < 0):hugou = 1
  else: hugou = -1
  a = abs(a)
  b = abs(b)
  G = gcd(a,b)
  return (hugou*(abs(a)//G),abs(b)//G)

C0 = collections.Counter()

for i in range(n):
  a,b = map(int,input().split())
  if (a,b) == (0,0) :count += 1
  else:
    a0,b0 = make_key0(a,b)
    C0[(a0,b0)] += 1

S = set()
for key,val in C0.items():
  a0,b0 = key
  S.add((a0,b0))
  a1,b1 = make_key0(b0,a0)
  if (a1,b1) in S:continue
  ans *= pow(2,val,mod) + pow(2,C0[(a1,b1)],mod) -1
  ans %= mod
ans += count 
print((ans-1)%mod)