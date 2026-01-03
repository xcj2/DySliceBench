def odd(n):
    return n % 2 == 1
    
def even(n):
    return n % 2 == 0

from math import factorial as fact
def c(n, r):
    if n < r:
        return 0
    if n == 0:
        return 0
    if r == 0:
        return 1
    return fact(n) // (fact(n-r) * fact(r))

n, p = map(int, input().split())
a = list(map(int, input().split()))
o = [i for i in a if odd(i)]
e = [i for i in a if even(i)]
x = len(o)
y = len(e)
yc = 0
for i in range(y):
    yc += c(y, i + 1)
ans = 0
if p == 0:
    ans += 1
i = 2 - p
while True:
    if i > x:
        break
    ans += c(x, i)
    ans += c(x, i) * yc
    i += 2
if p == 0:
    ans += yc
print(ans)