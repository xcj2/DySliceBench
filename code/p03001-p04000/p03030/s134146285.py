#	!/usr/bin/env python3
#	encoding: UTF-8
#	Modified: <26/May/2019 06:11:19 PM>


#	✪ H4WK3yE乡
#	Mohd. Farhan Tahir
#	Indian Institute Of Information Technology (IIIT), Gwalior


import sys


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return map(int, sys.stdin.readline().split())


def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    d = {}
    for i in range(n):
        x, y = input().split()
        if x not in d:
            d[x] = []
        d[x].append((int(y), i + 1))
    for i in d:
        d[i].sort(reverse=True)
    from collections import OrderedDict
    od = OrderedDict(sorted(d.items()))
    # print(od)
    for i in od:
        for j in od[i]:
            print(j[1])


if __name__ == "__main__":
    main()
