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
    H, W = readnums()
    a = [list(readstr()) for _ in range(H)]
    p = list()
    for i, aa in enumerate(a):
        if all([x == '.' for x in aa]):
            p.append(i)

    for i in reversed(p):
        a.pop(i)

    p = list()
    for i in range(W):
        c = [x[i] for x in a]
        if all([x == '.' for x in c]):
            p.append(i)

    for i in reversed(p):
        for aa in a:
            aa.pop(i)

    for aa in a:
        print(''.join(aa))


if __name__ == "__main__":
    main()
