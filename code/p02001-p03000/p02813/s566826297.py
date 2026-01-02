# -*- coding: utf-8 -*-
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
write = sys.stdout.write
import itertools
def ii(): return int(readline())
def mi(): return map(int, readline().rstrip().split())
def li(): return list(readline().rstrip())
def lmi(): return list(map(int, readline().rstrip().split()))
def end(*arg): print(*arg); sys.exit()
# template


def main():
    n = ii()
    P = tuple(lmi())
    Q = tuple(lmi())
    p, q = 0, 0
    a = [i + 1 for i in range(n)]
    for idx, l in enumerate(itertools.permutations(a, n)):
        if P == l:
            p = idx
        if Q == l:
            q = idx
    print(abs(p - q))
    return


if __name__ == '__main__':
    main()
