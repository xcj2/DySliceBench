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
    N, M = readnums()
    xy = [tuple(readnums()) for _ in range(M)]
    dic = {i: 1 for i in range(1, N + 1)}
    r = {1}
    for (x, y) in xy:
        dic[x] -= 1
        dic[y] += 1
        if x in r:
            r.add(y)
            if not dic[x]:
                r.remove(x)

    print(len(r))


if __name__ == "__main__":
    main()
