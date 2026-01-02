import math


def primes(x):
    x+=1
    if x < 2:
        return []

    prime = [i for i in range(x)]
    prime[1] = 0

    for p in prime:
        if p > math.sqrt(x):
            break
        if p == 0:
            continue
        for non_prime in range(2 * p, x, p):
            prime[non_prime] = 0

    return [p for p in prime if p != 0]


def over(l, x):
    ans = 0
    for i in range(len(l)):
        if l[i] >= x:
            ans += 1
    return ans


def combinations_count(n, r):
    return math.factorial(n)//(math.factorial(n-r) * math.factorial(r))


n = int(input())


p = primes(n)
r = [1 for i in range(len(p))]

for i in range(n):
    j = 0
    k = i+1
    while k!=1:
        while k%p[j]==0:
            r[j]+=1
            k//=p[j]
        j+=1

ans = 0

ans += over(r,75)

for i in range(len(r)):
    if r[i]>=25:
        ans += over(r,3)-1
    if r[i]>=15:
        ans += over(r,5)-1

o5 = over(r,5)
o3 = over(r,3)
if o5>=2 and o3>=3:
        ans += combinations_count(o5,2) * combinations_count(o3-2,1)

print(ans)


