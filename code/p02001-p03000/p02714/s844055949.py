#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/input.txt"
exit $?
'''
import sys


def _s(): return sys.stdin.readline().strip()


def _i(): return int(sys.stdin.readline().strip())


def main():
    n = _i()
    s = _s()
    c = {
        "R": [0] * (n + 1),
        "G": [0] * (n + 1),
        "B": [0] * (n + 1)
    }
    j = n
    for rgb in reversed(s):
        j -= 1
        for _rgb in "RGB":
            c[_rgb][j] = c[_rgb][j+1]
        c[rgb][j] += 1

    ans = 0
    rgb = {"R", "G", "B"}
    for i in range(n-2):
        c1 = s[i]
        for j in range(i+1, n-1):
            c2 = s[j]
            if c1 == c2:
                continue
            #
            c3 = (rgb - {c1, c2}).pop()
            ans += c[c3][j+1]
            k = 2 * j - i
            if k < n and s[k] == c3:
                ans -= 1
    return ans


if __name__ == "__main__":
    print(main())
