#!/bin/bash
''':'
docker run --rm -it -v $(cd $(dirname $0) && pwd):/vo:ro pypy:3-2.4.0 \
   /bin/bash -c "pypy3 /vo/$(basename $0) < /vo/input.txt"
exit $?
'''
import sys


def _i(): return int(sys.stdin.readline().strip())


def _gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    return _gcd(b, a % b)


def main():
    gcd = [[1]*201 for _ in range(201)]
    for i in range(1, 201):
        for j in range(i, 201):
            g = _gcd(i, j)
            gcd[i][j] = gcd[j][i] = g

    k = _i() + 1
    ans = 0
    for l in range(1, k):
        for m in range(1, k):
            glm = gcd[l][m]
            for n in range(1, k):
                ans += gcd[glm][n]
    return ans


if __name__ == "__main__":
    print(main())
