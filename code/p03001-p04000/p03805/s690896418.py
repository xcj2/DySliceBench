import sys
from itertools import permutations
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    N, M = readnums()
    ab = [list(readnums()) for _ in range(M)]
    l = range(2, N + 1)
    ans = 0
    for v in permutations(l):
        if [1, v[0]] in ab:
            flag = 1
            for i in range(N - 2):
                if [v[i], v[i + 1]] not in ab and [v[i + 1], v[i]] not in ab:
                    flag = 0

            if flag:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
