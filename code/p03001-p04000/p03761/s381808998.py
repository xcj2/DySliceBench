import sys
from string import ascii_lowercase
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
    S = [readstr() for _ in range(N)]
    cl = {x: 0 for x in ascii_lowercase}
    for i, s in enumerate(S):
        for x in ascii_lowercase:
            if not i:
                cl[x] = s.count(x)
            else:
                cl[x] = min(cl[x], s.count(x))
    print(''.join([k * v for k, v in sorted(cl.items(), key=lambda x: x[0])]))


if __name__ == "__main__":
    main()
