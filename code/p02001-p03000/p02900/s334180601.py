a, b = map(int, input().split())
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def common_divisors(k,j):
  c = make_divisors(k) + make_divisors(j)
  return [x for x in set(c) if c.count(x) > 1]

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
  
kouyakusuu = common_divisors(a,b)

aa=factorize(a)
bb=factorize(b)
l = list(set(aa))+list(set(bb))
ll = [x for x in set(l) if l.count(x) > 1]

print(len(ll)+1)