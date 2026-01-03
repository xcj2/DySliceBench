import sys
# sys.setrecursionlimit(100000)
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    nodes = defaultdict(int)
    for _ in range(m):
        a, b = input_int_list()
        nodes[a] += 1
        nodes[b] += 1

    for k, v in nodes.items():
        if v % 2 == 1:
            print("NO")
            return
    print("YES")

    return


if __name__ == "__main__":
    main()
