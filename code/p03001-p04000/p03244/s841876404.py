mod = 10 ** 9 + 7
mod2 = 2**61+1
from collections import deque
import heapq
from bisect import bisect_left, insort_left, bisect_right

_NUMINT_ALL = list(range(10))

def main():
    ans = solve()
    if ans is not None:
        print(ans)

def solve():
    N = iip(False)

    V = iip()
    v1 = V[1::2]
    v2 = V[::2]

    d1 = {}
    for i in v1:
        if i in d1:
            d1[i] += 1
        else:
            d1[i] = 1

    d2 = {}
    for i in v2:
        if i in d2:
            d2[i] += 1
        else:
            d2[i] = 1

    d1 = list(d1.items())
    d1.sort(key=lambda x:x[1])
    d2 = list(d2.items())
    d2.sort(key=lambda x:x[1])

    m11 = d1[-1][1]
    if len(d1) >= 2:
        m12 = d1[-2][1]
    else:
        m12 = 0

    m21 = d2[-1][1]
    if len(d2) >= 2:
        m22 = d2[-2][1]
    else:
        m22 = 0

    if d1[-1][0] != d2[-1][0]:
        return N - (d1[-1][1]+d2[-1][1])
    else:
        return min(N - (m11+m22), N - (m12+m21))


    #print(d1)
    #print(d2)


#####################################################ライブラリ集ここから

def iip(listed=True, num_only = True):
    if num_only:
        ret = [int(i) for i in input().split()]
    else:
        ret = [int(i) if i in _NUMINT_ALL else i for i in input().split()]

    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

def iipt(l, listed=False, num_only = True):
    ret = []
    for i in range(l):
        ret.append(iip_ord(listed=listed, num_only=num_only))
    return ret

def sortstr(s):
    return "".join(sorted(s))

def iip_ord():
    return [ord(i) - ord("a") for i in input()]

def YesNo(s):
    if s:
        print("Yes")
    else:
        print("No")

def fprint(s):
    for i in s:
        print(i)

def bitall(N):
    ret = []
    for i in range(2**N):
        a = []
        for j in range(N):
            a.append(i%2)
            i //= 2
        ret.append(a)
    return ret

def split_print_space(s):
    print(" ".join([str(i) for i in s]))

def split_print_enter(s):
    print("\n".join([str(i) for i in s]))


def koenai_saidai_x_index(sorted_list, n):
    l = 0
    r = len(sorted_list)
    if len(sorted_list) == 0:
        return False
    if sorted_list[0] > n:
        return False

    while r - l > 1:
        x = (l + r) // 2
        if sorted_list[x] == n:
            return x
        elif sorted_list[x] > n:
            r = x
        else:
            l = x
    return l


def searchsorted(sorted_list, n, side="left"):
    if side not in ["right", "left"]:
        raise Exception("sideはrightかleftで指定してください")

    l = 0
    r = len(sorted_list)

    if n > sorted_list[-1]:
        # print(sorted_list)
        return len(sorted_list)
    if n < sorted_list[0]:
        return 0

    while r - l > 1:
        x = (l + r) // 2
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


def soinsuu_bunkai(n):
    ret = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            ret.append(i)
        if i > n:
            break
    if n != 1:
        ret.append(n)
    return ret


def conbination(n, r, mod, test=False):
    if n <= 0:
        return 0
    if r == 0:
        return 1
    if r < 0:
        return 0
    if r == 1:
        return n
    ret = 1
    for i in range(n - r + 1, n + 1):
        ret *= i
        ret = ret % mod

    bunbo = 1
    for i in range(1, r + 1):
        bunbo *= i
        bunbo = bunbo % mod

    ret = (ret * inv(bunbo, mod)) % mod
    if test:
        # print(f"{n}C{r} = {ret}")
        pass
    return ret


def inv(n, mod):
    return power(n, mod - 2)


def power(n, p, mod_= mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_


if __name__ == "__main__":
    main()