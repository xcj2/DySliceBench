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

N = I()
b = LI()

ans = []
while b:
    n = len(b)
    flag = False
    for i in range(n)[::-1]:
        if b[i] == i+1:
            ans.append(i+1)
            flag = True
            break
    if not flag:
        print(-1)
        exit()
    b.pop(i)

for a in ans[::-1]:
    print(a)