import random
#a,bの最大公約数
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)


#nの約数列挙
def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass

#n以下の素数列挙(O(n log(n))
def primes(n):
    is_prime = [True] * (n + 100)
    is_prime[0] = False
    is_prime[1] = True
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

    return is_prime

def is_prime(n):
    if n == 1:
        return True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


a,b = map(int,input().split())

g = gcd(a,b)
d = divisor(g)
d.sort()

res = 0

#isp = primes(g)
#print(isp)

for e in d:
    if is_prime(e):
        res += 1

print(res)

