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
    A = [list(readnums()) for _ in range(3)]
    c = [[False] * 3 for _ in range(3)]
    N = readint()
    for i in range(N):
        a = readint()
        pos = [(x, y) for y, row in enumerate(A) for x, elem in enumerate(row) if A[x][y] == a]
        if pos:
            x, y = pos[0]
        else:
            continue
        c[x][y] = True

    if all(c[0]) or all(c[1]) or all(c[2]) or all([x[0] for x in c]) or all([x[1] for x in c]) or all([x[2] for x in c]) or all([x[i] for i, x in enumerate(c)]) or all([x[2 - i] for i, x in enumerate(c)]):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
