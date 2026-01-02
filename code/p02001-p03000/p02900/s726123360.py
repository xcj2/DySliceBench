# -*- coding: utf-8 -*-

# input
A, B = map(int, input().split())

# solve
def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    return gcd(r, b)

def divisor(n):
    i = 1
    l = list()
    while i * i <= n:
        if n % i == 0:
            l.append(i)
            l.append(n // i)
        i += 1
    l = list(set(l))
    return l

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

ans = list()
a = divisor(A)
b = divisor(B)
d = a + b
l = list()
for i in set(d):
    if d.count(i) > 1:
        l.append(i)

if len(l) > 1:
    ans.append(l[0])
    for i in range(1, len(l)):
        if is_prime(l[i]):
            ans.append(l[i])
else:
    ans = l

# output
print(len(ans))