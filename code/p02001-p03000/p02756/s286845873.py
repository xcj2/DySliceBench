#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/g.inp"
exit $?
'''
import sys
from collections import deque


def _s(): return sys.stdin.readline().strip()


def _sa(): return sys.stdin.readline().strip().split()


def _i(): return int(sys.stdin.readline().strip())


def main():
    s = deque([c for c in _s()])
    q = _i()
    flip = 0
    for _ in range(q):
        tmp = _sa()
        op = int(tmp[0])
        if op == 1:
            flip ^= 1
        else:
            loc = int(tmp[1]) - 1
            c = tmp[2]
            if flip ^ loc:
                s.append(c)
            else:
                s.appendleft(c)

    n = len(s)
    for _ in range(n):
        if flip == 0:
            print(s.popleft(), end="")
        else:
            print(s.pop(), end="")


if __name__ == "__main__":
    main()
