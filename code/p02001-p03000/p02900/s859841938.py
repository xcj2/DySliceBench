import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True
def gcd( x, y ):
    while y != 0:
        x, y = y, x%y
    return x

def coprime(a, b):
    return gcd(a, b) == 1

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
A , B = map(int , input().split())
#A = 100000000000
#B = 50000000000
#print(make_divisors(A))

gcd_value = gcd(A , B)
cd = []
div = make_divisors(gcd_value)

for i in range(len(div)):
    if A % div[i] == 0 and B % div[i] == 0 and is_prime(div[i]):
        cd.append(div[i])
print(len(cd) + 1)