import sys
from collections import Counter
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
    n = readint()
    v = list(readnums())
    ve = [x for i, x in enumerate(v) if not i % 2]
    vo = [x for i, x in enumerate(v) if i % 2]
    cve = Counter(ve)
    cvo = Counter(vo)
    if cve.most_common()[0][0] == cvo.most_common()[0][0]:
        if len(cve) == 1:
            print(n // 2)
        else:
            print(min(len(ve) - cve.most_common()[1][1] + len(vo) - cvo.most_common()[0][1], len(ve) - cve.most_common()[0][1] + len(vo) - cvo.most_common()[1][1]))
    else:
        print(len(ve) - cve.most_common()[0][1] + len(vo) - cvo.most_common()[0][1])


if __name__ == "__main__":
    main()
