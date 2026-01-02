import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
# sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    s = gete()

    a = (1 <= int(s[:2]) <= 12)
    b = (1 <= int(s[2:]) <= 12)

    if a:
        if b:
            print("AMBIGUOUS")
        else:
            print("MMYY")
    else:
        if b:
            print("YYMM")
        else:
            print("NA")


if __name__ == "__main__":
    main()
