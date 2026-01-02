import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math
from bisect import bisect_left

a, b = getList()

def koyak(a, b):
    koyak = []

    for i in range(1, int(math.sqrt(max(a, b))) + 1):
        if a % i == 0 and b % i == 0:
            koyak.append(i)

    return koyak

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

# ko = koyak(a, b)
ko = list((set(make_divisors(a)) & set(make_divisors(b))))
ko.sort()
ans = []
for k in ko:
    fl = True
    for an in ans:
        if k % an == 0 and an != 1:
            fl = False
            break
    if fl:
        ans.append(k)

# print(ko)
print(len(ans))