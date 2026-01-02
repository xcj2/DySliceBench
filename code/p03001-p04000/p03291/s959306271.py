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


mod = 10**9 + 7


def main():
    s = input()

    qsum = 0
    for c in s:
        if c == '?':
            qsum += 1

    ccount = defaultdict(int)
    qcount = defaultdict(int)

    for i in reversed(range(len(s))):
        if s[i] == 'C':
            ccount[i] = modadd(ccount[i+1], 1)
            qcount[i] = qcount[i+1]
        elif s[i] == '?':
            ccount[i] = ccount[i+1]
            qcount[i] = modadd(qcount[i+1], 1)
        else:
            ccount[i] = ccount[i+1]
            qcount[i] = qcount[i+1]

    bccount = defaultdict(int)
    qccount = defaultdict(int)
    bqcount = defaultdict(int)
    qqcount = defaultdict(int)

    for i in reversed(range(len(s) - 1)):
        if s[i] == 'A' or s[i] == 'C':
            bccount[i] = bccount[i+1]
            qccount[i] = qccount[i+1]
            bqcount[i] = bqcount[i+1]
            qqcount[i] = qqcount[i+1]
        elif s[i] == 'B':
            bccount[i] = modadd(bccount[i+1], ccount[i+1])
            qccount[i] = qccount[i+1]
            bqcount[i] = modadd(bqcount[i+1], qcount[i+1])
            qqcount[i] = qqcount[i+1]
        elif s[i] == '?':
            bccount[i] = bccount[i+1]
            qccount[i] = modadd(qccount[i+1], ccount[i+1])
            bqcount[i] = bqcount[i+1]
            qqcount[i] = modadd(qqcount[i+1], qcount[i+1])

    ans = 0

    for i in range(len(s) - 2):
        if s[i] == 'A':
            if bccount[i+1]:
                ans = modadd(ans, modmlt(bccount[i+1], pow(3, qsum, mod)))
            if qccount[i+1]:
                ans = modadd(ans, modmlt(qccount[i+1], pow(3, qsum - 1, mod)))
            if bqcount[i+1]:
                ans = modadd(ans, modmlt(bqcount[i+1], pow(3, qsum - 1, mod)))
            if qqcount[i+1]:
                ans = modadd(ans, modmlt(qqcount[i+1], pow(3, qsum - 2, mod)))
        if s[i] == '?':
            if bccount[i+1]:
                ans = modadd(ans, modmlt(bccount[i+1], pow(3, qsum - 1, mod)))
            if qccount[i+1]:
                ans = modadd(ans, modmlt(qccount[i+1], pow(3, qsum - 2, mod)))
            if bqcount[i+1]:
                ans = modadd(ans, modmlt(bqcount[i+1], pow(3, qsum - 2, mod)))
            if qqcount[i+1]:
                ans = modadd(ans, modmlt(qqcount[i+1], pow(3, qsum - 3, mod)))

    print(ans)


if __name__ == '__main__':
    main()
