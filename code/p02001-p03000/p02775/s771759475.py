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
    N = input()
    nl = [int(i) for i in N]
    nl.reverse()

    ret = 0
    b = nl[0]
    fin = len(nl) - 1
    for i in range(len(nl)):
        if i != fin:
            a = b
            b = nl[i + 1]
            if a >= 10:  # 繰り上がり処理
                a -= 10
                b += 1

            if a <= 4:
                ret += a  # その桁が4以下ならちょうど払う

            if a == 5:  # 1つ上の桁次第
                if b >= 5:
                    b += 1
                    ret += 5
                else:
                    ret += 5

            if a >= 6:  # 1つ上の桁の金で払う
                b += 1
                ret += (10 - a)

        else:
            if b <= 5:
                ret += b
                return ret
            if b >= 6:
                ret += 1 + (10 - b)
                return ret


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