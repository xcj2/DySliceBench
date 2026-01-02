n, m = map(int, input().split())
a = list(map(int, input().split()))

def f(x):
    res = 0
    while x % 2 == 0:
        x//= 2
        res += 1
    return res

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)

for i in range(n):
    a[i] //= 2

t = f(a[0])

ans = 0
for i in range(n):
    if f(a[i]) != t:
        print(0)
        exit()
    a[i] >>= t

m >>= t

l = 1
for i in range(n):
    l = lcm(l, a[i])
    if l > m:
        print(0)
        exit()

m //= l
ans = (m + 1)//2
print(ans)
