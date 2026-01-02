#!/usr/bin/env python
# -*- coding: utf-8 -*-


def print_array(a):
    print(" ".join(map(str, a)))


def selectionsort(arr, n):
    a = arr[:]
    s = 0
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        if i != minj:
            (a[i], a[minj]) = (a[minj], a[i])
            s += 1
    return (a, s)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    (a, s) = selectionsort(arr, n)
    print_array(a)
    print(s)


if __name__ == "__main__":
    main()