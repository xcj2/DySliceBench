import sys
from collections import defaultdict

input = sys.stdin.readline


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return list(MI())


def LIN(n: int):
    return [I() for _ in range(n)]


inf = float("inf")
mod = 10 ** 9 + 7


def main():
    n, m = MI()
    h = LI()

    dict = defaultdict(set)
    for _ in range(m):
        a, b = MI()
        dict[a].add(b)
        dict[b].add(a)

    c = n
    for k, v in dict.items():
        for t in v:
            if h[t - 1] >= h[k - 1]:
                c -= 1
                break

    print(c)


if __name__ == "__main__":
    main()
