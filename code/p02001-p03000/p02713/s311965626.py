from functools import reduce

# from collections import defaultdict


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def gcddd(*numbers):
    return reduce(gcd, numbers)


def reducef(x, y):
    return gcdd[(x, y)]


def gcd2(*numbers):
    return reduce(reducef, numbers)


K = int(input())
ans = 0
# gcdd=defaultdict()
gcdd = {}
for a in range(1, K + 1):
    for b in range(1, K + 1):
        if (a, b) not in gcdd:
            gcdd[(a, b)] = gcddd(a, b)

for a in range(1, K + 1):
    for b in range(1, K + 1):
        for c in range(1, K + 1):
            ans += gcd2(a, b, c)
print(ans)
