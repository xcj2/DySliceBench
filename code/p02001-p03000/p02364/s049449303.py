from sys import stdin
input = stdin.readline

from collections import defaultdict

MAX = 10000
infty = -1

class Disjoint():
    def __init__():
        return

def getRoot(x):
    global v
    for _ in range(v+1):
        if dic[x]["parent"] == x:
            return x
        x = dic[x]["parent"]

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

lines = stdin.readlines()
dic = defaultdict()
v, e = map(int, lines[0].split())
#E = [[lines[i+1].split()[0], lines[i+1].split()[1], lines[i+1].split()[2],] for i in range(e)]
E = [ list(map(int, lines[i+1].split())) for i in range(e)]
E = sorted(E, key=lambda x:x[2])

# Eの要素を整列
E = sorted(E, key=lambda x:x[2])
# V に対応した互に素な集合Sを生成する
for _ in range(v):
    dic[_] = {"rank":0,"parent":_}
# 辺の集合Kを空にする
k = 0
total = 0

for edge in E:
    if getRoot(edge[0]) != getRoot(edge[1]):
        unite(edge[0], edge[1])
        k += 1
        total += edge[2]

print(total)
    





