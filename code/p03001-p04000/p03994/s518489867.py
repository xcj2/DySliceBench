#!/usr/bin/env python3

ORD_A = ord("a")


def str2list(s):
    return list(map(lambda c: ord(c) - ORD_A, s))


def list2str(xs):
    return "".join(map(lambda x: chr(x + ORD_A), xs))


def find_min(s, k):
    def to_a_cost(x):
        return (26 - x) % 26
    xs = str2list(s)
    n = len(s)
    for i in range(n):
        c = to_a_cost(xs[i])
        if c <= k:
            k -= c
            xs[i] = 0
    k %= 26
    for i in range(n)[::-1]:
        if xs[i] != 0:
            xs[i] += k
            break
    else:
        xs[-1] += k
    return list2str(xs)


def main():
    s = input()
    k = int(input())
    print(find_min(s, k))


if __name__ == '__main__':
    main()
