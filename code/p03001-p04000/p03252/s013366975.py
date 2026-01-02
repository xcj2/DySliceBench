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
    S = readstr()
    T = readstr()

    sl = dict()
    tl = dict()
    for s, t in zip(S, T):
        if s not in sl:
            sl[s] = t
        else:
            if sl[s] != t:
                print('No')
                break

        if t not in tl:
            tl[t] = s
        else:
            if tl[t] != s:
                print('No')
                break
    else:
        print('Yes')


if __name__ == "__main__":
    main()
