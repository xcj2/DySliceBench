import math
import sys
n,m = map(int, input().split())
a = list(map(int, input().split()))

def gcd(x,y):
    if x < y:
        x,y = y,x
    while x%y != 0:
        x,y = y,x%y
    return y

def lcm(x,y):
    return x/gcd(x,y)*y

def f(x):
    count = 0
    while x%2 == 0:
        x /= 2
        count += 1
    return count

for i in range(n):
    if a[i]%2 == 1:
        print(0)
        sys.exit()
    a[i] /= 2

count = f(a[0])

for i in range(n):
    if f(a[i]) != count:
        print(0)
        sys.exit()
    a[i] /= 2**count
m /= 2**count

l = 1
for i in range(n):
    l = lcm(l,a[i])
    if l > m:
        print(0)
        sys.exit()
m /= l

ans = (m+1)/2
print(int(ans))
