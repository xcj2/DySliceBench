m = 100010
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
a = primes(m * 2+ 100)
n = int(input())

from bisect import bisect_left
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def do(x):
    if x in a and (x+1)//2 in a:
        return True
dat = [-1] * m
count = 0
for i in range(len(a)):
    if a[i] > m:
        break
    if do(a[i]):
        count += 1
    dat[a[i]] = count
c = -1
for i in range(m):
    if dat[i] != -1:
        c = dat[i]
    else:
        dat[i] = c
dat[0] = dat[1] = 0

for _ in range(n):
    l, r = map(int, input().split())
    print(dat[r] - dat[l-1])
