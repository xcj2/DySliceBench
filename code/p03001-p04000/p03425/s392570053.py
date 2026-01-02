import sys
from collections import Counter
from itertools import combinations


def input(): return sys.stdin.readline().strip()


def solve(S):
    c = Counter(S)

    # 文字が3種類未満
    if len(c.keys()) < 3:
        return 0

    # 人数が3人未満
    if sum(c.values()) < 3:
        return 0

    ans = 0
    for i, j, k in combinations('MARCH', 3):
        ans += c[i] * c[j] * c[k]

    return ans


def main():
    N = int(input())
    S = [input()[0] for _ in range(N)]
    print(solve(S))


if __name__ == "__main__":
    main()
