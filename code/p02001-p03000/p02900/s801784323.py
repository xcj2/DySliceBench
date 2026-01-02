def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
a,b=map(int,input().split())
sai=gcd(a,b)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

kou=make_divisors(sai)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

ans=0
for i in kou:
    if is_prime(i):
        ans+=1
print(ans+1)