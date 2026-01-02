mod = 10**9 + 7
def iip(listed = False):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

def inv(n, mod):
    return power(n, mod-2)

def conbination(n, r, mod, test=False):
    if n <=0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0

    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    #if test:
    #    print(f"{n}C{r} = {ret}")
    return ret

def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p//2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p-1)) % mod

def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret

N, K = iip()
A = iip(listed=True)
A.sort(reverse=True)



def main():
    plus = 0
    minus = 0

    a1Ck1 = conbination(N, K-1, mod) % mod
    for i, Ai in enumerate(A):
        if N-i < K:
            break
        a1Ck1 *= (N-K-i+1)
        a1Ck1 *= inv(N-i, mod)
        a1Ck1 %= mod

        plus += a1Ck1 * Ai

    A.sort(reverse=False)
    a1Ck1 = conbination(N, K-1, mod) % mod
    for i, Ai in enumerate(A):
        if N-i < K:
            break
        a1Ck1 *= (N-K-i+1)
        a1Ck1 *= inv(N-i, mod)
        a1Ck1 %= mod

        minus += a1Ck1 * Ai

    ans = plus-minus
    ans %= mod
    print(ans)


main()