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


def main():
    n, c = intin()
    dlistlist = [None]
    for _ in range(c):
        dlist = [None]
        dlist.extend(intina())
        dlistlist.append(dlist)
    clistlist = []
    for _ in range(n):
        clistlist.append(intina())

    costs0 = []
    costs1 = []
    costs2 = []

    for cc in range(1, c + 1):

        costs = [0, 0, 0]

        for i in range(n):
            for j in range(n):
                costs[(i + j) % 3] += dlistlist[clistlist[i][j]][cc]

        costs0.append((costs[0], cc))
        costs1.append((costs[1], cc))
        costs2.append((costs[2], cc))

    costs0.sort()
    costs1.sort()
    costs2.sort()

    ans = float('inf')
    for cost0, c0 in costs0[:3]:
        for cost1, c1 in costs1[:3]:
            for cost2, c2 in costs2[:3]:
                if c0 == c1 or c1 == c2 or c2 == c0:
                    continue
                ans = min(ans, cost0 + cost1 + cost2)

    print(ans)


if __name__ == '__main__':
    main()
