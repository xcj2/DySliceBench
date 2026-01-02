# 3.4.3

import re
from collections import deque
from functools import reduce
from heapq import *
from itertools import permutations
from math import pi
from operator import itemgetter
from operator import mul
from operator import xor
from os import linesep


def isprime(n: int) -> bool:
    if n <= 1:
        return False
    if n in (2, 3, 5):
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    lst = int(n**0.5)
    f = 5
    while f <= lst:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def strmat(matrix, lnsep: str = linesep, fieldsep: str = ' ') -> str:
    return lnsep.join(map(lambda row: fieldsep.join(map(str, row)), matrix))


def strbool(boolval: int) -> str:
    return ['No', 'Yes'][boolval]


def solve() -> None:
    # read here
    n, m, *t = map(int, open(0).read().split())

    # solve here
    d = [[] for i in range(m+1)]
    for i in range(n):
        a, b = t[2*i], t[2*i+1]
        if a > m:
            continue
        d[a].append(b)

    ans = 0
    tasks = []
    for t in range(m + 1):
        # from (m days after) to today
        for tasksize in d[t]:
            heappush(tasks, -tasksize)
        if tasks:
            # do task
            ans -= heappop(tasks)

    # print here
    print(ans)


if __name__ == '__main__':
    solve()
