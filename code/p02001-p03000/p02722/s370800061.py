n = int(input())
def make(r):
    rr = [1]
    for i, v in r:
        newrr = rr[:]
        for j in rr:
            for k in range(v):
                newrr.append(j * i ** (k + 1))
        rr = newrr
    return rr
        
def factors(n):
    k = n
    i = 2
    r = []
    while i * i <= k:
        v = 0
        while k % i == 0:
            v += 1
            k //= i
        if v > 0:
            r.append((i, v))
        i += 1
    if k > 1:
        r.append((k, 1))
    return make(r)

def isOK(n, k):
    return n % k == 1

r = 0
for i in factors(n):
    n1 = n
    while n1 % i == 0 and i != 1:
        n1 //= i
    if isOK(n1, i):
        r += 1
#print(factors(n), r)
r += len(factors(n - 1)) - 1
#print(factors(n - 1), r)
print(r)
