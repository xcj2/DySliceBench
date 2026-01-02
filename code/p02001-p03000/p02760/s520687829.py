#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/g.inp"
exit $?
'''
import sys


def _i(): return int(sys.stdin.readline().strip())


def _ia(): return [int(x) for x in sys.stdin.readline().strip().split()]


def judge(a):
    for aij in ai:
        if aij not in b:
            flag = False
            break


def main():
    a = [_ia() for _ in range(3)]

    n = _i()
    b = [_i() for _ in range(n)]
    f1 = True
    f4 = True
    for i in range(3):
        if a[i][i] not in b: f1 = False
        if a[i][-1-i] not in b: f4 = False

        f2, f3 = [True] * 2
        for j in range(3):
            if a[i][j] not in b: f2 = False
            if a[j][i] not in b: f3 = False
        if f2 or f3: return "Yes"
    return "Yes" if f1 or f4 else "No"


if __name__ == "__main__":
    print(main())
