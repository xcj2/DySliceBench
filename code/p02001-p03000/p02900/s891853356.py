A, B = map(int, input().split())

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

G = gcd(A, B)
l = make_divisors(G)
l.remove(1)
if len(l) == 0:
    print(1)
else:
    c = 1
    for i in range(len(l)):
        for j in range(i):
            if not coprime(l[i], l[j]):
                break
        else:
            c += 1
    print(c)