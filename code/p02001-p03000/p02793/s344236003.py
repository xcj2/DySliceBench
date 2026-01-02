mod = 10**9 + 7
def iip(listed = False):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

def inv(n, mod):
    return power(n, mod-2)

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

n = iip()
A = iip(listed=True)

def main():
    ss = []
    for a_i in A:
        for s in ss:
            if a_i % s == 0:
                a_i //= s

        ss.extend(soinsuu_bunkai(a_i))

    #print(ss)
    all = 1
    for s in ss:
        all *= s
        all %= mod

    ans = 0
    for a_i in A:
        ans += (all * inv(a_i, mod)) % mod
        ans %= mod
    print(ans)


main()