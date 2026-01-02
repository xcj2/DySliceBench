from sys import stdin
input = stdin.readline

from collections import defaultdict

n, q = map(int, input().split())

dic = defaultdict()









def getRoot(x):
    global n
    for _ in range(n+1):
        if dic[x]["parent"] == x:
            return x
        x = dic[x]["parent"]

def makeSet(x):
    return


def unite(x, y):
    r = getRoot(x)
    l = getRoot(y)
    a = dic[r]["rank"]
    b = dic[l]["rank"]

    if a == b:
        dic[r]["rank"] += 1
        dic[l]["parent"] = r

    elif a > b:
        dic[l]["rank"] = 0
        dic[l]["parent"] = r

    elif a < b:
        dic[r]["rank"] = 0
        dic[r]["parent"] = l

for _ in range(n):
    dic[_] = {"rank":0,"parent":_}

for _ in range(q):
    com , x, y = map(int, input().split())
    if com == 0:
        unite(x, y)

    else:
        s = getRoot(x)
        t = getRoot(y)
        if s == t :
            print('1')
        else:
            print('0')
