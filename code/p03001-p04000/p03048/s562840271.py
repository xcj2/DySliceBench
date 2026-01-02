###############################################################################

from sys import stdout
import sys
from bisect import bisect_left as binl
from copy import copy, deepcopy


mod = 1


def intin():
    input_tuple = input().split()
    if len(input_tuple) <= 1:
        return int(input_tuple[0])
    return tuple(map(int, input_tuple))


def intina():
    return [int(i) for i in input().split()]


def intinl(count):
    return [intin() for _ in range(count)]


def modadd(x, y):
    global mod
    return (x + y) % mod


def modmlt(x, y):
    global mod
    return (x * y) % mod


def lcm(x, y):
    while y != 0:
        z = x % y
        x = y
        y = z
    return x


def combination(x, y):
    assert(x >= y)

    if y > x // 2:
        y = x - y

    ret = 1

    for i in range(0, y):
        j = x - i
        i = i + 1

        ret = ret * j
        ret = ret // i

    return ret


def get_divisors(x):
    retlist = []
    for i in range(1, int(x**0.5) + 3):
        if x % i == 0:
            retlist.append(i)
            retlist.append(x // i)
    return retlist


def get_factors(x):
    retlist = []
    for i in range(2, int(x**0.5) + 3):
        while x % i == 0:
            retlist.append(i)
            x = x // i
    retlist.append(x)
    return retlist


def make_linklist(xylist):
    linklist = {}
    for a, b in xylist:
        linklist.setdefault(a, [])
        linklist.setdefault(b, [])
        linklist[a].append(b)
        linklist[b].append(a)
    return linklist


def calc_longest_distance(linklist, v=1):
    distance_list = {}
    distance_count = 0
    distance = 0
    vlist_previous = []
    vlist = [v]
    nodecount = len(linklist)

    while distance_count < nodecount:
        vlist_next = []
        for v in vlist:
            distance_list[v] = distance
            distance_count += 1
            vlist_next.extend(linklist[v])
        distance += 1
        vlist_to_del = vlist_previous
        vlist_previous = vlist
        vlist = list(set(vlist_next) - set(vlist_to_del))

    max_distance = -1
    max_v = None
    for v, distance in distance_list.items():
        if distance > max_distance:
            max_distance = distance
            max_v = v

    return (max_distance, max_v)


def calc_tree_diameter(linklist, v=1):
    _, u = calc_longest_distance(linklist, v)
    distance, _ = calc_longest_distance(linklist, u)
    return distance


###############################################################################

cache = {}


def calc_pattern2(x, a, b):
    global cache

    if (x, a, b) in cache:
        return cache[(x, a, b)]
    if x < 0:
        return 0
    if x == 0:
        return 1

    ans = 0

    ans += calc_pattern2(x - a - b, a, b)

    if x % a == 0:
        ans += 1
    if x % b == 0:
        ans += 1

    cache[(x, a, b)] = ans
    return ans


def calc_pattern3(x, a, b, c):
    global cache

    if (x, a, b, c) in cache:
        return cache[(x, a, b, c)]
    if x < 0:
        return 0
    if x == 0:
        return 1

    ans = 0

    ans += calc_pattern3(x - a - b - c, a, b, c)

    ans += calc_pattern2(x - a - b, a, b)
    ans += calc_pattern2(x - b - c, b, c)
    ans += calc_pattern2(x - c - a, c, a)

    if x % a == 0:
        ans += 1
    if x % b == 0:
        ans += 1
    if x % c == 0:
        ans += 1

    cache[(x, a, b, c)] = ans
    return ans


def main():
    sys.setrecursionlimit(5000)
    r, g, b, n = intin()
    print(calc_pattern3(n, r, g, b))


if __name__ == '__main__':
    main()
