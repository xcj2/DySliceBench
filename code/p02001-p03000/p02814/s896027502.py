def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(*x):
    result = 1
    for x0 in x:
        d = gcd(result, x0)
        result = result // d * x0
    return result

def p_adic_valuation(n, p):
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result

N, M = map(int, input().split())
a = list(map(int, input().split()))

def solve():
    v = p_adic_valuation(a[0], 2)
    for i in range(1, N):
        if p_adic_valuation(a[i], 2) != v:
            return 0
    assert v > 0
    X_min = lcm(*a) // 2
    return M // X_min - M // (2 * X_min)

print(solve())