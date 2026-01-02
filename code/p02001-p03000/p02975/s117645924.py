import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())

from collections import defaultdict

n = ni()
a = list(li())

dic = defaultdict(int)

for ai in a:
    dic[ai] += 1

if len(dic) > 3:
    print("No")

elif len(dic) == 3:
    keys = []
    vals = []
    for k, v in dic.items():
        keys.append(k)
        vals.append(v)

    if vals[0] == vals[1] == vals[2] and keys[0] ^ keys[1] ^ keys[2] == 0:
        print("Yes")

    else:
        print("No")

elif len(dic) == 2:
    if not 0 in dic.keys():
        print("No")

    else:
        zero = dic[0]
        anot = 0
        for k, v in dic.items():
            if k != 0:
                anot = v

        if zero * 2 != anot:
            print("No")

        else:
            print("Yes")

elif len(dic) == 1:
    if not 0 in dic.keys():
        print("No")

    else:
        print("Yes")

