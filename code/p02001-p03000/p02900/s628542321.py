def gcd(x, y):
    a, b = x, y
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b

def divisors(x):
    D = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            D.append(i)
            if i != x**0.5:
                D.append(x // i)
    D.sort()
    return D

def isprime(x):
    t = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            t = 0
            break
    if t == 1 and x != 1:
        return True
    else:
        return False


a, b = map(int, input().split())

CD = divisors(gcd(a, b))

ans = 1
for cd in CD:
    if isprime(cd):
        ans += 1

print(ans)
