from functools import reduce

def gcd_base(x, y):
    if x % y:
        return gcd_base(y, x%y)
    return y

def gcd(numbers):
    return reduce(gcd_base, numbers)

def lcm_base(x, y):
    res = (x * y) // gcd_base(x, y)
    return res if res <= 1000000007 else 0

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
k = [0] * n
for i in range(n):
    j = a[i]
    while(j%2==0):
        j //= 2
        k[i] += 1
if any([k[i]!=k[i+1] for i in range(n-1)]):
    print(0)
else:
    l = [i//2 for i in a]
    x = lcm(l)
    if x==0:
        print(0)
    else:
        print((m//x+1)//2)