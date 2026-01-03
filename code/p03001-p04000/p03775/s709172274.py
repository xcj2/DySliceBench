
import collections
import itertools
import sys

def getint(): return int(input())
def getints(): return list(map(int, input().split()))

def get_divisor(n):
    if n == 1:
        return [1]
    res = []
    for i in range(1, n):
        if i * i > n:
            break
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n//i)
    return res

n=getint()
divs=get_divisor(n)
res = 10
for d1 in divs:
    d2 = n // d1
    tmp = max(len(str(d1)), len(str(d2)))
    res = min(res, tmp)

print(res)