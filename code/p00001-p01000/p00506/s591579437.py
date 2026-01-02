# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0583

"""
import sys
from sys import stdin
from itertools import combinations
from functools import reduce
input = stdin.readline



def solve2():
    divs = [1]
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    for i in range(2, a+1):
        while a%i == 0 and b%i == 0:
            divs.append(i)
            a //= i
            b //= i

    t = divs[:]
    for i in range(2, len(divs)):
        for c in combinations(divs[1:], i):
            p = reduce(lambda x, y: x*y, c)
            t.append(p)
    st = list(set(t))
    st.sort()
    return st


def solve3():
    divs = [1]
    A = [int(x) for x in input().split()]
    A.sort()
    a, b, c = A[0], A[1], A[2]

    for i in range(2, a+1):
        while a%i == 0 and b%i == 0 and c%i == 0:
            divs.append(i)
            a //= i
            b //= i
            c //= i

    t = divs[:]
    for i in range(2, len(divs)):
        for combi in combinations(divs[1:], i):
            p = reduce(lambda x, y: x*y, combi)
            t.append(p)
    st = list(set(t))
    st.sort()
    return st


def main(args):
    num = int(input())
    if num == 2:
        result = solve2()
    else:
        result = solve3()
    print('\n'.join(map(str, result)))


if __name__ == '__main__':
    main(sys.argv[1:])
    