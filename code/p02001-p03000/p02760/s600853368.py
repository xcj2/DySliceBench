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

    if all(c[0]) or all(c[1]) or all(c[2]) or all([c[0][0], c[1][0], c[2][0]]) or all([c[0][1], c[1][1], c[2][1]]) or all([c[0][2], c[1][2], c[2][2]]) or all([c[0][0], c[1][1], c[2][2]]) or all([c[2][0], c[1][1], c[0][2]]):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
