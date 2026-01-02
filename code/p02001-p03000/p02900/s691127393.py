def divisors(n):
    i = 1
    table = set()
    while i * i <= n:
        if not n % i:
            table.add(i)
            table.add(n//i)
        i += 1
    return table

def max2(x,y):
    return x if x > y else y

def rec(start_set, t):
    global res
    res = max2(res, t)
    next_set = []
    i = start_set[0]
    for j in start_set[1:]:
        if gcd(data[i], data[j]) == 1:
            next_set.append(j)
    if next_set:
        rec(next_set, t+1)
    return res

from math import gcd

A, B = map(int, input().split())
data = divisors(A) & divisors(B)
data = list(data)
data.sort()
L = len(data)
res = 0
print(rec(list(range(L)),1))



