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


class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.root(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        rooti = self.root(i)
        rootj = self.root(j)
        if rooti == rootj:
            return
        if rooti < rootj:
            self.parent[rootj] = rooti
        else:
            self.parent[rooti] = rootj

    def same(self, i, j):
        return self.root(i) == self.root(j)


###############################################################################


def main():
    h, w = intin()
    slistlist = ['#' * (w + 2)]
    slistlist.extend(['#' + input() + '#' for _ in range(h)])
    slistlist.append('#' * (w + 2))

    clistlist = []
    for i in range(h + 2):
        clistlist.append([False] * (w + 2))

    white_count = 0
    for slist in slistlist:
        for s in slist:
            if s == '.':
                white_count += 1

    paths = {(1, 1): 1}

    while paths:
        next_paths = defaultdict(lambda: float('inf'))

        for p, c in paths.items():
            if slistlist[p[0]+1][p[1]] == '.' and not clistlist[p[0]+1][p[1]]:
                next_paths[(p[0]+1, p[1])] = min(c + 1, next_paths[(p[0]+1, p[1])])
                clistlist[p[0]+1][p[1]] = True
            if slistlist[p[0]-1][p[1]] == '.' and not clistlist[p[0]-1][p[1]]:
                next_paths[(p[0]-1, p[1])] = min(c + 1, next_paths[(p[0]-1, p[1])])
                clistlist[p[0]-1][p[1]] = True
            if slistlist[p[0]][p[1]+1] == '.' and not clistlist[p[0]][p[1]+1]:
                next_paths[(p[0], p[1]+1)] = min(c + 1, next_paths[(p[0], p[1]+1)])
                clistlist[p[0]][p[1]+1] = True
            if slistlist[p[0]][p[1]-1] == '.' and not clistlist[p[0]][p[1]-1]:
                next_paths[(p[0], p[1]-1)] = min(c + 1, next_paths[(p[0], p[1]-1)])
                clistlist[p[0]][p[1]-1] = True

        paths = next_paths
        if (h, w) in paths:
            print(white_count - paths[(h, w)])
            return

    print(-1)


if __name__ == '__main__':
    main()
