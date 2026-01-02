N,M = input().split()
N = int(N)
M = int(M)

def prime_decomposition(n):
    i = 2
    table = []
    counter = []
    while i * i <= n:
        count = 0
        while n % i == 0:
            n /= i
            table.append(int(i))
            count += 1
        counter.append(count)
        i += 1
    count = 0
    if n > 1:
        table.append(int(n))
        count += 1
        counter.append(count)
    return table, counter

nCr = {}
def cmb(n, r):
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]


def cmb_(n, r):
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


table, counter = prime_decomposition(M)
result = 1

for i in counter:
    a = cmb_(int(i)+int(N)-1,int(N)-1)

    result *= a

print(result%(10**9+7))