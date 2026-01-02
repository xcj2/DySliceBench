import sys
input = sys.stdin.buffer.readline

import math

n = int(input())
mod = 1000000007
AB = []
for i in range(n):
    a, b = map(int, input().split())
    AB.append((a, b))

def power(a, n, mod):
  bi=str(format(n,"b")) #2進数
  res=1
  for i in range(len(bi)):
    res=(res*res) %mod
    if bi[i]=="1":
      res=(res*a) %mod
  return res

def toid(a, b):
    flag = False
    if a == 0 and b == 0:
        return (0, 0)
    elif a == 0:
        return (0, 1)
    elif b == 0:
        return (1, 0)
    else:
        if a > 0 and b > 0:
            g = math.gcd(a, b)
            a //= g
            b //= g
        elif a > 0 and b < 0:
            b = -b
            g = math.gcd(a, b)
            a //= g
            b //= g
            b = -b
        elif a < 0 and b > 0:
            a = -a
            g = math.gcd(a, b)
            a //= g
            b //= g
            b = -b
        else:
            a = -a
            b = -b
            g = math.gcd(a, b)
            a //= g
            b //= g
        return (a, b)

def totg(a, b):
    if a == 0 and b == 0:
        return (0, 0)
    elif a == 0:
        return (1, 0)
    elif b == 0:
        return (0, 1)
    else:
        if a > 0 and b > 0:
            g = math.gcd(a, b)
            a //= g
            b //= g
            t = (b, -a)
        elif a > 0 and b < 0:
            b = -b
            g = math.gcd(a, b)
            a //= g
            b //= g
            b = -b
            t = (-b, a)
        elif a < 0 and b > 0:
            a = -a
            g = math.gcd(a, b)
            a //= g
            b //= g
            a = -a
            t = (b, -a)
        else:
            a = -a
            b = -b
            g = math.gcd(a, b)
            a //= g
            b //= g
            a = -a
            b = -b
            t = (-b, a)
        return t


d = {}
ans = 0
for i in range(n):
    a, b = AB[i]
    s = toid(a, b)
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1

ans = 1
used = set()
for k1, v1 in d.items():
    if k1 in used:
        continue
    if k1 == (0, 0):
        continue
    a, b = k1
    k2 = totg(a, b)
    if k2 in d:
        v2 = d[k2]
    else:
        v2 = 0
    temp = power(2, v1, mod)-1+power(2, v2, mod)-1+1
    ans *= temp
    ans %= mod
    used.add(k1)
    used.add(k2)

ans -= 1
if (0, 0) in d:
    ans += d[(0, 0)]

print(ans%mod)