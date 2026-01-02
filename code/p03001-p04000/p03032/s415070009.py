mod = 10 ** 9 + 7
from collections import deque
import heapq


def iip(listed):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret


def main():
    r = solve()
    print(r)


def solve():
    N, K = iip(False)
    V = iip(True)

    gsize = N+1

    dp1 = [[None for i in range(gsize)] for i in range(gsize)]
    dp1[0][0] = 0
    for i, value in enumerate(V, 1):
        for j in range(gsize):
            if dp1[i-1][j] is not None:
                dp1[i][j] = dp1[i-1][j] + value

            v = dp1[i-1][j-1]
            if j >= 1 and dp1[i-1][j-1] is not None:
                vv = dp1[i][j]
                if vv is not None:
                    v = max(v, vv)
                dp1[i][j] = v

    V.reverse()
    dp2 = [[None for i in range(gsize)] for i in range(gsize)]
    dp2[0][0] = 0
    for i, value in enumerate(V, 1):
        for j in range(gsize):
            if dp2[i - 1][j] is not None:
                dp2[i][j] = dp2[i - 1][j] + value

            v = dp2[i - 1][j - 1]
            if j >= 1 and dp2[i - 1][j - 1] is not None:
                vv = dp2[i][j]
                if vv is not None:
                    v = max(v, vv)
                dp2[i][j] = v

    mm = 0
    for i1 in range(gsize):
        for j1 in range(gsize):
            for i2 in range(gsize):
                for j2 in range(gsize):
                    if dp1[i1][j1] is None:
                        continue
                    if dp2[i2][j2] is None:
                        continue

                    kh = dp1[i1][j1]+dp2[i2][j2]
                    if i1 + i2 + j1 + j2 > K:
                        continue
                    if i1 + i2 > N:
                        continue

                    mm = max(kh, mm)


    #for j in dp1:
    #    print(j)
    #for j in dp2:
    #    print(j)

    return mm


#####################################################ライブラリ集ここから

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


def searchsorted(sorted_list, n, side):
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


def power(n, p):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2) ** 2) % mod
    if p % 2 == 1:
        return (n * power(n, p - 1)) % mod


if __name__ == "__main__":
    main()