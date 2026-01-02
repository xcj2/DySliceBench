import sys
import math
from collections import defaultdict
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def LI(): return list(map(int, input().split()))
def LIR(row,col):
    if row <= 0:
        return [[] for _ in range(col)]
    elif col == 1:
        return [I() for _ in range(row)]
    else:
        read_all = [LI() for _ in range(row)]
        return map(list, zip(*read_all))

#################

# N=20000のとき，2の倍数と3の倍数を全て採用
# 6の倍数をペアにして適当に削る

N = I()

def output(X,Y):
    for y in Y:
        X.append(y[0])
        X.append(y[1])
    print(*X)
    return

X = []
Y = []
y2 = []
y3 = []
for i in range(2,30001):
    if i%6 == 0:
        X.append(i)
    else:
        if i%2 == 0:
            y2.append(i)
        elif i%3 == 0:
            y3.append(i)
        else:
            pass
        if len(y2) == 2:
            Y.append(y2)
            y2 = []
        if len(y3) == 2:
            Y.append(y3)
            y3 = []

a = 20000-N

if a == 19997:
    print(2,5,63)
elif a == 19996:
    print(2,5,20,63)
else:
    if a >= 5000:
        if a%2 == 0:
            for _ in range((a-5000)//2):
                Y.pop()
            output([],Y)
        else:
            for _ in range((a-4999)//2):
                Y.pop()
            output([6],Y)
    else:
        for _ in range(a-a//2*2):
            X.pop()
        for _ in range(a//2):
            Y.pop()
        output(X,Y)