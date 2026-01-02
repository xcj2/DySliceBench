import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N = I()
B = make_divisors(N - 1)
b = len(B)

A = make_divisors(N)

cnt = 0
for i in range(1, len(A) // 2 + 1):
    x = A[i]
    y = A[-i - 1]
    while y > x:
        if (y - 1) % x == 0:
            cnt += 1
            break
        elif y % x == 0:
            y //= x
        else:
            break
    if y == x:
        cnt += 1

ans = b - 1 + cnt + 1
print(ans)