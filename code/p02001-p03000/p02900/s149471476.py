A, B = [int(x) for x in input().split()]

def common_divisors(a, b):
    cd = []
    n = min(a, b)
    m = max(a, b)
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if m % i == 0:
                cd.append(i)
            if i != n // i and m % (n//i) == 0:
                cd.append(n//i)
    return cd

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def sieve(n):
    prime = []
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return prime


cd = common_divisors(A, B)
#prime = sieve(max(cd))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if i*i > n:
            break
        if n % i == 0:
            return False
    return True

#print(cd)
#print(max(cd))
#print(prime)

ans = 1 # 1は絶対入る
for a in cd:
    if is_prime(a):
        ans += 1

print(ans)
