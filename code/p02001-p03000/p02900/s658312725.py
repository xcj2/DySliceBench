a, b = map(int, input().split())

# get GCD(Gratest Common Divisor: 最大公約数)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# get divisors(公約数)
def divisors(n):
    nums = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            nums.append(i)
            if i != n // i:
                nums.append(n//i)
    return sorted(nums)

# is prime(Prime Number: 素数)
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0: return False
    return True

x = divisors(gcd(a, b))

ans = 1
for _x in x:
    ans += is_prime(_x)

print(ans)
