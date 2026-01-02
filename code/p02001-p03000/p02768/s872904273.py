mod = 1000000007

def mul(a, b):
    return ((a % mod) * (b % mod)) % mod

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y // 2) ** 2 % mod
    else:
        return power(x, y // 2) ** 2 * x % mod

def div(a, b):
    return mul(a, power(b, mod - 2))

def combination(n,r):
    bumbo = 1
    bunshi = 1
    for i in range(r):
        bumbo = (bumbo*(n-i)) % mod
    for i in range(1,r+1):
        bunshi = (bunshi*i) % mod
    return (div(bumbo, bunshi)) % mod


n, a, b = map(int, input().split())
print((power(2,n)-1-combination(n,a)-combination(n,b)) % mod)