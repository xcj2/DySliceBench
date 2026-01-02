###############################################################################

from sys import stdout
from bisect import bisect_left as binl
from copy import copy, deepcopy
from collections import defaultdict


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


def calc_partsum(asumlist, start, end):
    floor = start
    bound = (start + end) // 2
    ceil = end - 1
    ret = (float('inf'), None, None)

    while True:
        p = asumlist[bound - 1] - asumlist[start - 1]
        q = asumlist[end - 1] - asumlist[bound - 1]

        if p == q:
            return p, q
        ret = min(ret, (abs(p - q), p, q))
        if floor >= ceil:
            _, p, q = ret
            return p, q

        if p > q:
            ceil = bound - 1
        if p < q:
            floor = bound + 1
        bound = (floor + ceil) // 2


def calc_sadness(asumlist, n, k):
    p, q = calc_partsum(asumlist, 1, k)
    r, s = calc_partsum(asumlist, k, n)
    return max([p, q, r, s]) - min([p, q, r, s])


def main():
    n = intin()
    alist = intina()

    asum = 0
    asumlist = [0]
    for a in alist:
        asum += a
        asumlist.append(asum)

    ans = float('inf')
    for i in range(3, n):
        ans = min(ans, calc_sadness(asumlist, n + 1, i))
    print(ans)


if __name__ == '__main__':
    main()
