a,b=list(map(int, input().split()))
def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def md(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

def coprime(a, b):
    return gcd(a, b) == 1

c = md(gcd(a,b))
c.sort()
if len(c)== 1:
    count = 1
else:
    count = 1
    d = c[0]
    for i in c[1:]:
        if coprime(d, i):
            d = d*i
            count += 1
        else:
            continue

print(count)