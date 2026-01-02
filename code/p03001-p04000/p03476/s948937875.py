from math import sqrt, ceil

cache = {3}
primes = {2,3}
def isprime(n):
    if n in primes:
        return True
    for i in range(3, ceil(sqrt(n))+1, 2):
        if n % i == 0:
            return False
    primes.add(n)
    return True

def prepare():
    l = 5
    r = 10**5-1
    for n in range(l, r+1, 4):
        if n in cache:
            continue
        m = (n - 1) // 2
        if isprime(m+1) and isprime(n):
            cache.add(n)

def solve(l, r):
    cnt = 0
    if l <= 3 <= r:
        cnt = 1
        l = 5
    if l % 4 == 3:
        l += 2
    for n in range(l, r+1, 4):
        if n in cache:
            cnt += 1
            continue
        m = (n - 1) // 2
        assert n % 4 == 1
        if isprime(m+1) and isprime(n):
            cache.add(n)
            cnt += 1
    return cnt

def main():
    global cache
    from bisect import bisect_left, bisect_right
    cache = sorted(cache)
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        i = bisect_left(cache, l)
        j = bisect_right(cache, r)
        print(j-i)

prepare()
main()
