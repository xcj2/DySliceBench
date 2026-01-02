n = int(input())
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
def divisor_num(n):
    a = 1
    for _, x in factorization(n):
        a *= x + 1
    return a
ans = 0
for i in range(1,n+1,2):
  d = divisor_num(i)
  if d == 8:
    ans +=1
print(ans)