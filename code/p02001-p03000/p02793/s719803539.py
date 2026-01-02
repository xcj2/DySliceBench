# from random import randint

MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))
# N = 10000
# A = [randint(1, 10**6) for _ in range(N)]

def modinv(a):
    return pow(a, MOD-2, MOD)

# a = 12345678900000
# b = 100000
# a %= MOD
# print(a * modinv(b) % MOD)

def gcd(a, b):
    if a > b:
        a, b = b, a
    if a == 0:
        return b
    return gcd(b%a, a)
def lcm(a, b):
    return (a * b) // gcd(a, b)

a_lcm = A[0]
for a_i in A[1:]:
    a_lcm = lcm(a_lcm, a_i)
a_lcm %= MOD

sum_num = 0
for a_i in A:
    sum_num = (sum_num + (a_lcm * modinv(a_i))) % MOD

print(sum_num)