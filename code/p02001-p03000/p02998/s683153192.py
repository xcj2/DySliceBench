import bisect
import heapq
import sys
import queue


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class V:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)

    def get(self):
        return self.v


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(x, X, VX):
    visit_node = [set(), set()]
    visit_link = set()

    q = queue.Queue()
    q.put((0, x))
    while not q.empty():
        p, s = q.get()
        if s in visit_node[p]:
            continue

        visit_node[p].add(s)
        VX[p][s] = True
        for t in X[p][s]:
            l = (s, t) if p == 0 else (t, s)
            if l in visit_link:
                continue
            visit_link.add(l)

            if t in visit_node[1 - p]:
                continue
            q.put((1 - p, t))

    return len(visit_node[0]) * len(visit_node[1]) - len(visit_link)


def main():
    N = int(input())
    X = {}
    Y = {}

    for _ in range(N):
        x, y = read_values()
        x -= 1
        y -= 1
        X.setdefault(x, set()).add(y)
        Y.setdefault(y, set()).add(x)

    VX = [False] * (10 ** 5)
    VY = [False] * (10 ** 5)

    res = 0
    for x in X.keys():
        if VX[x]:
            continue

        res += f(x, [X, Y], [VX, VY])

    for y in Y.keys():
        if VY[y]:
            continue

        res += f(y, [Y, X], [VY, VX])

    print(res)


if __name__ == "__main__":
    main()
