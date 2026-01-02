#!/usr/bin/env python
# -*- coding: utf-8 -*-


def print_array(a):
    print(" ".join(map(str, a)))


def bubblesort(a, n):
    swap = 0
    flag = True
    while flag:
        flag = False
        for j in range(n - 1, 0, -1):
            if a[j] < a[j - 1]:
                (a[j], a[j - 1]) = (a[j - 1], a[j])
                swap += 1
                flag = True
    return (a, swap)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    (b, swap) = bubblesort(a, n)
    print_array(b)
    print(swap)

if __name__ == "__main__":
    main()