# -*- coding: utf-8 -*-
from itertools import combinations

n = int(input())

f = []

for _ in range(n):
    line = list(map(lambda n:int(n),input().split(" ")))
    f.append(line)

p = []
for _ in range(n):
    line = list(map(lambda n:int(n),input().split(" ")))
    p.append(line)

def overlap(ary1,ary2):
    ret = 0
    for i in range(len(ary1)):
        if ary1[i]==ary2[i] and ary1[i]==1:
            ret += 1
    return ret

def calcProf(jary):
    # 各時間帯で店を開くかどうかの情報を元に、利益を計算する
    ret = 0
    for i in range(n):
        lap = overlap(jary, f[i])
        ret += p[i][lap]
    return ret

def conv(ary):
    ret = [0 for _ in range(10)]
    for i in ary:
        ret[i] = 1
    return ret

prof = -1000000000
for e in range(1,11):
    for elem in combinations(range(10), e):
        cp = calcProf(conv(elem))
        if cp>prof:
            prof = cp

print(prof)
