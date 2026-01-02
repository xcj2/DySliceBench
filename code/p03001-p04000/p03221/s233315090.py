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
    n, m = MI()
    cities = []
    prefes = [1]*(n+1)
    for i in range(m):
        a, b = MI()
        cities.append([b, a,  i])

    cities.sort()

    for i in range(m):
        city = cities[i]
        pref = city[1]
        pref_id = str(pref).zfill(6)
        sequence_id = str(prefes[pref]).zfill(6)
        prefes[pref] += 1
        res_id = pref_id + sequence_id
        cities[i].append(res_id)

    cities.sort(key=lambda x: x[2])

    for i in range(m):
        print(cities[i][-1])


main()
