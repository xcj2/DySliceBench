mod = 10**9 + 7

def iip(listed = False):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

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


def conbination(n, r, mod, test=False):
    if n <=0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n-r+1, n+1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r+1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        #print(f"{n}C{r} = {ret}")
        pass
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

#####################################################ライブラリ集ここまで

def main():
    N, X, Y = iip()
    X, Y = sorted((X-1, Y-1))
    #print(X, Y)

    result = [0 for i in range(1, N)]
    for a in range(0, N):
        for b in range(a+1, N):
            d1 = b-a
            d2 = abs(X-a)+abs(Y-b)+1
            d = min(d1, d2)-1
            #print(a, b, d)

            result[d] += 1

    print("\n".join([str(i) for i in result]))


if __name__ == "__main__":
    main()