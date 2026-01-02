mod = 10**9 + 7
from collections import deque

def main():
    S = input()

    ln = len(S)
    tl = []
    for i in range(ln):
        if i <= ln-1-1 and S[i] == "R" and S[i+1] == "L":
            tl.append(i)

    result = [0 for i in range(ln)]
    #print(tl)
    for i in range(ln):
        if S[i] == "R":
            tp_index = searchsorted(tl, i, "left")
            tp = tl[tp_index]
            if tp % 2 == i % 2:
                result[tp] += 1
            else:
                result[tp+1] += 1

        else:
            tp_index = searchsorted(tl, i, "left") - 1
            tp = tl[tp_index]

            if tp % 2 == i % 2:
                result[tp] += 1
            else:
                result[tp + 1] += 1

    split_print_space(result)




#####################################################ライブラリ集ここから

def split_print_space(s):
    print(" ".join([str(i) for i in s]))

def split_print_enter(s):
    print("\n".join([str(i) for i in s]))


def searchsorted(sorted_list, n, side):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    if n > sorted_list[-1]:
        #print(sorted_list)
        return len(sorted_list)
    if n < sorted_list[0]:
        return 0

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
        if sorted_list[l] == n:
            return r - 1
        else:
            return r

    if side == "right":
        if sorted_list[l] == n:
            return l + 1
        else:
            return l


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