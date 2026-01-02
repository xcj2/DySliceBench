# 3.5.2

import re
from collections import deque
from functools import reduce
from itertools import permutations
from math import pi
from operator import itemgetter
from operator import mul
from operator import xor
from os import linesep
from queue import PriorityQueue
from sys import stdin


def rline() -> str:
    return stdin.readline().strip()


def rlines(hint: int = 1):
    ret = ['' for i in range(hint)]
    for i in range(hint):
        ret[i] = rline()
    return ret


def htokens(hint: int = 1):
    lns = rlines(hint)
    ret = list(map(lambda ln: ln.split(), lns))
    # if return value has one and only one element(list),
    if hint == 1:
        # then add an empty list.
        ret.append([])
    return ret


def vtokens(hint: int = 1):
    m, _ = htokens()
    wint = len(m)
    ret = [[None] * hint for i in range(wint)]
    for y in range(hint):
        if y != 0:
            m, _ = htokens()
        # convert horizontal to vertical
        x = 0
        for v in m:
            ret[x][y] = v
            x += 1
    # if return value has one and only one element(list),
    if wint == 1:
        # then add an empty list.
        ret.append([])
    return ret


def rint(radix: int = 10) -> int:
    return int(rline(), radix)


def hints(hint: int = 1, radix: int = 10):
    ret = htokens(hint)
    for i in range(len(ret)):
        ret[i] = list(map(lambda v: int(v, radix), ret[i]))
    return ret


def vints(hint: int = 1, radix: int = 10):
    ret = vtokens(hint)
    for i in range(len(ret)):
        ret[i] = list(map(lambda v: int(v, radix), ret[i]))
    return ret


def mat(hint: int, wint: int):
    return [[None]*wint for i in range(hint)]


def filllist(lst, value: int) -> None:
    # destructive.
    for i in range(len(lst)):
        lst[i] = value


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
    (a, b), _ = hints()

    # solve here
    ans = max([a+b, a-b, a*b])

    # print here
    print(ans)


if __name__ == '__main__':
    solve()
