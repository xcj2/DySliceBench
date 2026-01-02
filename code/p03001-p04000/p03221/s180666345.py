#!/usr/bin/env python3

class City:
    def __init__(self, i1, p, y, o=None):
        self.i1 = i1
        self.p = p
        self.y = y
        self.o = o

    # def __repr__(self):
    #     return f"City({self.i1}, {self.p}, {self.y}, {self.o})"

    def get_id(self):
        return "%06d%06d" % (self.p, self.o)

def put_ids(n, cities):
    years = {i: [] for i in range(1, n + 1)}
    for c in cities:
        years[c.p].append(c.y)

    year_to_order = {i: {} for i in range(1, n + 1)}
    for i in range(1, n + 1):
        ys = sorted(years[i])
        for j0, y in enumerate(ys):
            year_to_order[i][y] = j0 + 1

    for c in cities:
        c.o = year_to_order[c.p][c.y]

def main():
    n, m = map(int, input().split())
    cities = []
    for i0 in range(m):
        p, y = map(int, input().split())
        city = City(i0, p, y)
        cities.append(city)
    put_ids(n, cities)
    for c in cities:
        print(c.get_id())

main()
