from collections import defaultdict
from collections import deque
from string import ascii_uppercase
import sys, bisect, math, heapq

stdin = sys.stdin
read_int = lambda : list(map(int,stdin.readline().split()))
read_str = lambda : stdin.readline().rstrip()

A, B = read_int()

# 約数列挙 return set
def divisor(n):
    res = []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
        i += 1
    return res

def gcd(a, b):
    if a > b:
        a, b = b, a
    while b % a != 0:
        a, b = b % a, a
    return a

# 素数判定 return bool
def is_prime(n):
    i = 2
    while i**2 <= n:
        if n % i == 0: return False
        i += 1
    return True

def solve():
    ans = 0

    g = gcd(A, B)
    koubai = divisor(g)

    for n in koubai:
        if is_prime(n):
            ans += 1
    return ans

if __name__ == "__main__":
    print(solve())