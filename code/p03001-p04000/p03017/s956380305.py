import sys
from collections import defaultdict
readline = sys.stdin.buffer.readline
#sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def main():
    n, a, b, c, d = geta(int)
    s = "#" + gete()

    if c < d:
        # no consecutive rocks between [a,c] and [b,d]
        if "##" in s[a:c + 1] or "##" in s[b:d + 1]:
            print("No")
        else:
            print("Yes")
    else:
        # no consecutive rocks between [a,c] and,
        # [b-1,d+1] contains "..."

        if (not "##" in s[a:c + 1]) and "..." in s[b - 1:d + 2]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()