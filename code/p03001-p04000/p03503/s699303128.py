import sys
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
    N = readint()
    F = [''.join(readstrs()) for _ in range(N)]
    P = [list(readnums()) for _ in range(N)]
    ans = -(10 ** 9)
    for i in range(1, 1024):
        val = 0
        for j, f in enumerate(F):
            c = bin(i & int(f, 2))[2:]
            v = sum(map(int, c))
            val += P[j][v]

        ans = max(ans, val)

    print(ans)


if __name__ == "__main__":
    main()
