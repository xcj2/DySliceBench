import sys

input = lambda: sys.stdin.readline()


def cin_int_list():
    return [int(x) for x in input().split()]


def cin_int_iter():
    return (int(x) for x in input().split())


def cin_int():
    return int(input())


def cout_int_iter(a):
    print(' '.join(map(str, a)))


def iota(n, start=0):
    return list(range(start, n))


def cin_digits_list():
    return [ord(x) - ord('0') for x in input()]


def main():
    n, k = cin_int_iter()

    g = {}

    for u, x in enumerate(cin_int_list()):
        v = x - 1
        g[u] = v

    visited = set()

    u = 0
    while u not in visited:
        visited.add(u)
        u = g[u]

    cycle_starts = u

    u = cycle_starts
    cycle = []
    while True:
        cycle.append(u)
        u = g[u]

        if u == cycle_starts:
            break

    before_cycle = []
    u = 0

    while u != cycle_starts:
        before_cycle.append(u)
        u = g[u]

    if k < len(before_cycle):
        print(before_cycle[k] + 1)
        return

    if before_cycle:
        k -= len(before_cycle)

    print(cycle[k % len(cycle)] + 1)




main()


"""
6 1
6 5 2 5 3 2

6 2
6 5 2 5 3 2

6 3
6 5 2 5 3 2

6 4
6 5 2 5 3 2

6 6
6 5 2 5 3 2

6 5
6 5 2 5 3 2


no cycle

4 1
2 3 4 5

4 111111111111111111
2 3 4 1

1 111111111111111111
1

2 1999999999999999999
2 1

3 99999999999999999999
2 3 2

3 99999999999999999999
2 3 4
"""