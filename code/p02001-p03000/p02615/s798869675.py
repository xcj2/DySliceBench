#!/usr/bin/env python3
import sys
import collections


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    As = LI()
    As.sort()
    As.reverse()
    As = collections.deque(As)
    ans = []
    tmp = As.popleft()
    ans.append(tmp)

    for i in range(len(As)):
        tmp = As.popleft()
        ans.extend([tmp, tmp])

    print(sum(ans[:N-1]))
    # print(ans)


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
