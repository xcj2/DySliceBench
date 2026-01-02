mod = 10 ** 9 + 7
mod2 = 2**61+1
from collections import deque
import heapq
from bisect import bisect_left, insort_left, bisect_right

def iip(listed=True):
    ret = [int(i) for i in input().split()]
    if len(ret) == 1 and not listed:
        return ret[0]
    return ret

def iip_ord():
    return [ord(i) - ord("a") for i in input()]


def main():
    ans = solve()
    if ans is not None:
        print(ans)

def solve():
    N, T = iip()

    dp1 = [[0 for _ in range(T)] for _ in range(N + 1)]
    dp2 = [[0 for _ in range(T)] for _ in range(N + 1)]
    AB = [iip() for i in range(N)]


    for i, ab in enumerate(AB, 1):
        a, b = ab
        for j in range(T):
            dp1[i][j] = dp1[i-1][j]
        for j in reversed(list(range(T))):
            if j+a >= T:
                continue
            dp1[i][j + a] = max(dp1[i][j + a], dp1[i][j] + b)


    for i, ab in enumerate(reversed(AB), 1):
        a, b = ab
        for j in range(T):
            dp2[i][j] = dp2[i-1][j]
        for j in reversed(list(range(T))):
            if j + a >= T:
                continue
            dp2[i][j + a] = max(dp2[i][j + a], dp2[i][j] + b)

    #dp2.reverse()

    mm = 0
    for i in range(N):
        for j in range(T):
            ii1 = i
            ii2 = N-i-1
            ii3 = i

            ij1 = j
            ij2 = T-j-1

            a = dp1[ii1][ij1]
            b = dp2[ii2][ij2]
            c = AB[ii3][1]
            #print(ii1, ii2, ij1, ij2, ii3, a, b, c, a+b+c)
            #print(a, b, c)
            mm = max(a+b+c, mm)


            #print(i, j, cur, a, b)


    #print(dp1)
    #print(dp2)

    print(mm)


#####################################################ライブラリ集ここから

def fprint(s):
    for i in s:
        print(i)

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


def power(n, p, mod_= mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_


if __name__ == "__main__":
    main()