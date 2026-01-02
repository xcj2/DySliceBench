#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/input.txt"
exit $?
'''
import sys


def _i(): return int(sys.stdin.readline().strip())


def _ia(): return map(int, sys.stdin.readline().strip().split())


def main():
    n, m = _ia()
    h = list(_ia())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = _ia()
        adj[a-1].append(b-1)
        adj[b-1].append(a-1)
    ans = 0
    for i in range(n):
        hi = h[i]
        f = True
        for j in adj[i]:
            hj = h[j]
            if hi <= hj:
                f = False
                break
        if f:
            ans += 1
    return ans


if __name__ == "__main__":
    print(main())
