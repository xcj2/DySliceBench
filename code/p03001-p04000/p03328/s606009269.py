import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


a, b = readints()
#print(a, b)
sum = 0
x = []
for i in range(1, 1000):
    sum += i
    x.append(sum)
# print(x)

for i in range(998):
    if x[i]-a == x[i+1]-b:
        print(x[i]-a)
        exit()
