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
n = int(input())
a = 1
for i in range(1,n+1):
  a*=i
x = factorization(a)
y = []
for i,j in x:
  y.append(j)
ans = 0
for i in y:
  if i >= 74:
    ans += 1
san = 0
go = 0
for i in y:
  if i >= 2:
    san += 1
  if i >= 4:
    go += 1
for i in y:
  if i>=24:
    ans += san-1
  if i >= 14:
    ans += go-1
ans += go*(go-1)//2*(san-2)
print(ans)