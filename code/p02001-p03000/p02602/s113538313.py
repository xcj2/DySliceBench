#
#    ------------------------------------------------
#           ____          _     Generatered using
#          / ___|        | |
#         | |    __ _  __| | ___ _ __  ______ _
#         | |   / _` |/ _` |/ _ \ '_ \|_  / _` |
#         | |__| (_| | (_| |  __/ | | |/ / (_| |
#          \____\____|\____|\___|_| |_/___\____|
#
#      GNU Affero General Public License v3.0
#    ------------------------------------------------
#    Author   : prophet
#    Created  : 2020-07-25 08:11:03.732018
#    UUID     : ZonihA5OmAzqBLgc
#    ------------------------------------------------
#
production = True

import sys, math, collections

def input(f = 0, m = 0):

    if m > 0: return [input(f) for i in range(m)]
    else:
        l = sys.stdin.readline()[:-1]

        if f >= 10:
            u = False
            f = int(str(f)[-1])
        else: u = True

        if f == 0: p = [l]
        elif f == 1: p = list(map(int, l.split()))
        elif f == 2: p = list(map(float, l.split()))
        elif f == 3: p = list(l)
        elif f == 4: p = list(map(int, list(l)))
        elif f == 5: p = l.split()

        return p if u else p[0]

def out(l, f = 0, n = True):

    if f == 0: p = str(l)
    elif f == 1: p = " ".join(map(str, l))
    elif f == 2: p = "\n".join(map(str, l))
    elif f == 3: p = "".join(map(str, l))

    print(p, end = "\n" if n else "")

def log(*args):
    if not production:
        print("$$$", end = "")
        print(*args)

enu = enumerate
ter = lambda a, b, c: b if a else c
ceil = lambda a, b: -(-a // b)
flip = lambda a: (a + 1) & 1

def mapl(i, f = 0):

    if f == 0: return list(map(int, i))
    elif f == 1: return list(map(str, i))
    elif f == 2: return list(map(list, i))

#
#   >>>>>>>>>>>>>>> START OF SOLUTION <<<<<<<<<<<<<<
#


def solve():

    n, k = input(1)
    a = input(1)

    for i in range(n - k):
        out(ter(a[i + k] > a[i], "Yes", "No"))

    return


solve()

#
#   >>>>>>>>>>>>>>>> END OF SOLUTION <<<<<<<<<<<<<<<
#
