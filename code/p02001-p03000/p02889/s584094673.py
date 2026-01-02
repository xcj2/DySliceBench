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
    N, M, L = iip()

    dis_table = [[10 ** 12 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dis_table[i][i] = 0

    for i in range(M):
        a, b, c = iip()
        a -= 1
        b -= 1
        if c <= L:
            dis_table[a][b] = c
            dis_table[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dis_table[i][j] = min(dis_table[i][j], dis_table[i][k] + dis_table[j][k])

    #print(dis_table)

    nt = [[10 ** 12 for _ in range(N)] for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if dis_table[i][j] <= L:
                nt[i][j] = 1

    for i in range(N):
        nt[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                nt[i][j] = min(nt[i][j], nt[i][k] + nt[j][k])

    q = iip(False)
    ans = []

    for i in range(q):
        a, b = iip()
        c = nt[a-1][b-1]
        if c == 10**12:
            ans.append(-1)
        else:
            ans.append(c-1)

    split_print_enter(ans)


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


def power(n, p, mod_= mod):
    if p == 0:
        return 1
    if p % 2 == 0:
        return (power(n, p // 2, mod_) ** 2) % mod_
    if p % 2 == 1:
        return (n * power(n, p - 1, mod_)) % mod_


if __name__ == "__main__":
    main()