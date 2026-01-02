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
    X, Y, A, B, C = iip()
    p = iip(listed=True)
    p.extend([0 for i in range(10**6)])
    q = iip(listed=True)
    q.extend([0 for i in range(10**6)])
    r = iip(listed=True)

    p.sort(reverse=True)
    q.sort(reverse=True)
    r.sort(reverse=True)

    red = p[:X]
    blue = q[:Y]
    red.sort()
    blue.sort()

    ir = 0
    ib = 0
    for nocolor in r:
        if min(red[ir], blue[ib]) < nocolor:
            if red[ir] < blue[ib]:
                red[ir] = nocolor
                if ir <= len(red)-2:
                    ir += 1
            else:
                blue[ib] = nocolor
                if ib <= len(blue)-2:
                    ib +=1
        else:
            break

    print(sum(red)+sum(blue))



    pass

if __name__ == "__main__":
    main()