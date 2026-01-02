a, b = map(int, input().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

agcd = gcd(a,b)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False

    return True

x = make_divisors(agcd)
ans = 1
for _x in x:
    ans += is_prime(_x)

print(ans)
