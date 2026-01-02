# https://atcoder.jp/contests/abc138/tasks/abc138_d

from collections import defaultdict
import sys
sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, q = input_int_list()
    cnt = [0] * (n + 1)  # 1-indexed
    tree = defaultdict(list)

    for _ in range(n - 1):
        a, b = input_int_list()
        tree[a].append(b)
        tree[b].append(a)

    # 遅延評価をする O(q)
    for _ in range(q):
        p, x = input_int_list()
        cnt[p] += x

    # 遅延評価（DFS）O(n)
    stack = [(1, 0)]
    visited = set([1])
    while stack:
        e, add = stack.pop()
        cnt[e] += add
        for node in tree[e]:
            if node not in visited:
                visited.add(node)
                stack.append((node, cnt[e]))

    print(" ".join([str(i) for i in cnt[1:]]))
    return


if __name__ == "__main__":
    main()
