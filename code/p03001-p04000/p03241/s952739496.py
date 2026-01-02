import math
n,m = map(int,input().split())
MAX = m//n
ans = 1
def factorization(n):
    def factor_sub(n, m):
        c = 0
        while n % m == 0:
            c += 1
            n /= m
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
a = divisor(m)
for i in a:
  if i <= MAX:
    ans = i
print(int(ans))