# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    n, k, l = map(int, input().split())
    p, q = [], []
    for _ in range(k):
        pi, qi = map(int, input().split())
        p.append(pi)
        q.append(qi)
    r, s = [], []
    for _ in range(l):
        ri, si = map(int, input().split())
        r.append(ri)
        s.append(si)

    road_tree = make_union_find(p, q, n)
    rail_tree = make_union_find(r, s, n)

    a, b = [], []
    x = defaultdict(int)
    for i in range(n):
        a.append(root(road_tree, i))
        b.append(root(rail_tree, i))
        key = (a[i], b[i])
        x[key] += 1

    for i in range(n):
        print(x[(a[i], b[i])], end=' ')

    # print("\n")
    # print(road_tree)
    # print(rail_tree)


def make_union_find(a, b, n):
    union_find_tree = [i for i in range(n)]

    for i in range(len(a)):
        x = root(union_find_tree, a[i] - 1)
        y = root(union_find_tree, b[i] - 1)
        if x != y:
            union_find_tree[x] = min(x, y)
            union_find_tree[y] = union_find_tree[x]

    return union_find_tree


# def make_union_find(a, b, n):
#     x = [i for i in range(n)]

#     for i in range(len(a)):
#         root = a[i] - 1
#         leaf = b[i] - 1
#         x[leaf] = root
#     return x


def root(union_find_tree, target):
    if union_find_tree[target] == target:
        return target
    else:
        union_find_tree[target] = root(
            union_find_tree, union_find_tree[target])
        return union_find_tree[target]


if __name__ == '__main__':
    main()
