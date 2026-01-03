def solve_abc065d():
    from collections import namedtuple
    from operator import attrgetter
    from itertools import tee
    import sys

    input = sys.stdin.readline

    City = namedtuple('City', 'x y idx')
    Edge = namedtuple('Edge', 'cost a b')
    N = int(input())

    cities = []
    for city_idx in range(N):
        x, y = map(int, input().split())
        c_ = City(x, y, city_idx)
        cities.append(c_)
    cities_x_asc = sorted(cities, key=attrgetter('x'))
    cities_y_asc = sorted(cities, key=attrgetter('y'))

    edges = []

    it_x = iter(cities_x_asc)
    gx1, gx2 = tee(it_x, 2)
    next(gx2)
    for c1, c2 in zip(gx1, gx2):
        d_ = c2.x - c1.x
        e_ = Edge(d_, c1.idx, c2.idx)
        edges.append(e_)
    # x方向にN-1本の辺を張る

    it_y = iter(cities_y_asc)
    gy1, gy2 = tee(it_y, 2)
    next(gy2)
    for c1, c2 in zip(gy1, gy2):
        d_ = c2.y - c1.y
        e_ = Edge(d_, c1.idx, c2.idx)
        edges.append(e_)
    # y方向にN-1本の辺を張る

    edges.sort(key=attrgetter('cost'))

    # <Kruskal’s Algorithm>
    # https://tjkendev.github.io/procon-library/python/graph/min_st_kruskal.html
    # E = [(cost, v, w), ...]
    #   G上の全ての辺(v, w)とそのcostを含むlist

    # Union-Findを使うことで頂点間の連結判定を行う
    *p, = range(N)

    def root(x):
        if x == p[x]:
            return x
        p[x] = y = root(p[x])
        return y

    def unite(x, y):
        px = root(x)
        py = root(y)
        if px == py:
            return 0
        if px < py:
            p[py] = px
        else:
            p[px] = py
        return 1

    mi = 0
    for e_ in edges:
        if unite(e_.a, e_.b):
            mi += e_.cost

    # miが最小全域木の解

    print(mi)
    return


if __name__ == '__main__':
    solve_abc065d()
