import sys
import numpy as np
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
    N, K = readnums()
    h = np.sort(np.array([readint() for _ in range(N)]))
    ans = 0
    for i in range(N - K + 1):
        if not i:
            ans = h[i + K - 1] - h[i]
        else:
            ans = min(ans, h[i + K - 1] - h[i])

    print(ans)


if __name__ == "__main__":
    main()
