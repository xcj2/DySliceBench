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
    sp = [readstrs() for _ in range(N)]
    S = list(map(lambda x: x[0], sp))
    t = {x: [] for x in S}
    for v in sp:
        t[v[0]].append(v[1])

    for k in t.keys():
        t[k] = sorted(list(map(int, t[k])), reverse=True)

    for k, v in sorted(t.items()):
        for vv in v:
            print(sp.index([k, str(vv)]) + 1)


if __name__ == "__main__":
    main()
