#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    la = []
    n_best = 0
    best = 0
    best2 = 0
    for i in range(n):
        a = ri()
        la.append(a)
        if best < a:
            best2 = best
            best = a
            n_best = 1
        elif best == a:
            n_best += 1
        else:
            best2 = max(best2, a)
    for a in la:
        if a < best:
            print(best)
        else:
            if n_best > 1:
                print(best)
            else:
                print(best2)


if __name__ == '__main__':
    main()
