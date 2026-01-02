
from math import sqrt, ceil

primes = [2]
for n in range(3, 101):
    if any(n % i == 0 for i in range(2, n)):
        continue
    primes.append(n)

def fact(n):
    p = 1
    for i in range(2, n+1):
        p *= i
    return p

def calc_factors(n):
    factors = {}
    for p in primes:
        while n % p == 0:
            factors[p] = factors.get(p, 0)+1
            n //= p
    return factors

def solve(N):
    n = fact(N)
    factors = calc_factors(n)

    nums = {3:0,5:0,15:0,25:0,75:0}
    for p, c in factors.items():
        if c >= 2:
            nums[3] = nums.get(3,0)+1
        if c >= 4:
            nums[5] = nums.get(5,0)+1
        if c >= 14:
            nums[15] = nums.get(15,0)+1
        if c >= 24:
            nums[25] = nums.get(25,0)+1
        if c >= 74:
            nums[75] = nums.get(75,0)+1
    print(sum([
            nums[5] * (nums[5] - 1) * (nums[3]-2) // 2,
            nums[15] * (nums[5] - 1) ,
            nums[25] * (nums[3] - 1) ,
            nums[75] ]))
N = int(input())
solve(N)
