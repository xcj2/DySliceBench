import sys
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
a.sort()
yaku = set()


import math
def factorization(n):
    def factor_sub(n, m):
        c = 0
        while n % m == 0:
            c += 1
            n //= m
        return c, n
    #
    buff = []
    c, m = factor_sub(n, 2)
    if c > 0: buff.append((2, c))
    c, m = factor_sub(m, 3)
    if c > 0: buff.append((3, c))
    x = 5
    while m >= x * x:
        c, m = factor_sub(m, x)
        if c > 0: buff.append((x, c))
        if x % 6 == 5:
            x += 2
        else:
            x += 4
    if m > 1: buff.append((m, 1))
    return buff
#a = factorization(n)
#b = []
#for i,j in a:
#  b.append(i)
def divisor_sub(p, q):
    a = []
    for i in range(0, q + 1):
        a.append(p ** i)
    return a

def divisor(n):
    if n == 1:
      return([1])
    xs = factorization(n)
    ys = divisor_sub(xs[0][0], xs[0][1])
    for p, q in xs[1:]:
        ys = [x * y for x in divisor_sub(p, q) for y in ys]
    return sorted(ys)
#素因数列挙
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n //= i
      table.append(i)
    i += 1
  if n > 1:
    table.append(n)
  table = set(table)
  table = list(table)
  return table


a1 =divisor(a[0])
a2 = divisor(a[1])
for i in a1:
    yaku.add(i)
for i in a2:
    yaku.add(i)
yaku = list(yaku)
yaku.sort()
yaku = yaku[::-1]
for i in yaku:
    flag = 1
    for j in range(n):
        if a[j] % i == 0:
            continue
        else:
            if flag:
                flag = 0
            else:
                break
    else:
        print(i)
        exit()