def gcds(*numbers):
    from math import gcd
    from functools import reduce
    return reduce(gcd, numbers)

def lcms(*numbers):
    from math import gcd
    from functools import reduce
    def lcm_base(x, y):
        return x // gcd(x, y) * y
    return reduce(lcm_base, numbers)

def build_inv(N=10**5, P=10**9+7):
    inv = [0, 1]
    for i in range(2, N + 1):
        inv.append((-inv[P % i] * (P // i)) % P)
    return inv

def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9+7
    invs = build_inv(10**6, MOD)
    target = lcms(*A)
    print(target*sum(map(lambda x: invs[x], A))%MOD)

    
if __name__ == "__main__":
    resolve()

