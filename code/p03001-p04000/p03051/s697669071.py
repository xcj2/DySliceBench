###############################################################################

from sys import stdout
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


mod = 10**9 + 7


class Counter:
    def __init__(self, zerocount):
        self.incr = 1
        self.prev_zerocount = zerocount
        self.count = 1


def main():
    n = intin()
    alist = intina()

    xorlist = []
    xor = 0
    for a in alist:
        xor = a ^ xor
        xorlist.append(xor)

    zerocount = 0
    counters = {}

    for xor in xorlist:
        if xor == 0:
            zerocount += 1
            continue
        if xor not in counters:
            counters[xor] = Counter(zerocount)
            continue

        prev_incr = counters[xor].incr
        prev_zerocount = counters[xor].prev_zerocount
        prev_count = counters[xor].count

        incr = modmlt(zerocount - prev_zerocount, prev_count)
        incr = modadd(incr, prev_incr)

        counters[xor].incr = incr
        counters[xor].prev_zerocount = zerocount
        counters[xor].count = modadd(prev_count, incr)

    if xorlist[-1]:
        print(counters[xorlist[-1]].incr)
    else:
        zerosum = pow(2, zerocount - 1, mod)
        xorsum = sum([counter.count for counter in counters.values()]) % mod
        print(modadd(zerosum, xorsum))


if __name__ == '__main__':
    main()
