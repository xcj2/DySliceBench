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

def next_digit(i):
    if i == 0:
        return [0,1]
    elif i == 9:
        return [8,9]
    else:
        return [i-1,i,i+1]

K = I()

q = [1,2,3,4,5,6,7,8,9]
n = len(q)
num = 0
while q:
    q1 = []
    for v in q:
        num += 1
        if num == K:
            print(v)
            exit()
        for u in next_digit(int(str(v)[-1])):
            q1.append(10*v+u)
    q = q1