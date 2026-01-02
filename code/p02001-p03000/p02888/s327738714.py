mod = 10**9 + 7

def main():
    N = iip(listed=False)
    L = iip(True)
    L.sort()

    ret = 0
    for i in range(N):
        for j in range(i+1, N):
            minl = L[j]-L[i]
            maxl = L[j]+L[i]

            left = searchsorted(L, minl, "right")
            left = max(j+1, left)

            right = searchsorted(L, maxl, "left")

            #print(L[i], L[j], left, right)

            #print(i, j, left, right)
            ret += (right-left)
    print(ret)




#####################################################ライブラリ集ここから

def searchsorted(sorted_list, n, side):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    while r-l > 1:
        x = (l+r)//2
        if sorted_list[x] > n:
            r = x
        elif sorted_list[x] < n:
            l = x
        else:
            if side == "left":
                r = x
            elif side == "right":
                l = x

    if side == "left":
        return r
    if side == "right":
        return l+1



def iip(listed):
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


if __name__ == "__main__":
    main()