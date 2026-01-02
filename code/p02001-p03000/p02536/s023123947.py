#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N, M = MI()

    routes = []

    cities = [[] for i in range(N)]

    for i in range(M):
        a, b = MI()
        cities[a-1].append(b-1)
        cities[b-1].append(a-1)

    groups = [-1] * N

    group = 0

    for i in range(N):
        if groups[i] != -1:
            continue
        deque = cl.deque([i])
        groups[i] = group
        while len(deque) > 0:
            city = deque.popleft()
            next_cities = cities[city]
            for next_city in next_cities:
                if groups[next_city] != -1:
                    continue
                groups[next_city] = group
                deque.append(next_city)

        group += 1

    print(group - 1)


main()
