import math
import collections
def trial_division_sqrt(n):

    prime_count = collections.Counter()

    for i in range(2, int(math.sqrt(n)) + 2):
        while n % i == 0:
            n /= i
            prime_count[i] += 1
    if n > 1:
        prime_count[n] += 1

    return prime_count
def pc(n, r):
    return math.factorial(n) // (math.factorial(n - r)  * math.factorial(r))
nCr = {}
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n;

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p;
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result;
s=0
x,N = map(int,input().split())

li = trial_division_sqrt(N)
li = li.most_common()
ans = 1
for i in range(0, len(li)):
    ans *= cmb(li[i][1] + x-1, x-1)
print(ans % (pow(10, 9)+7))