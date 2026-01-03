import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[]]*num
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

#インデックス付きソート
#(index,value)の順に格納
from operator import itemgetter
def index_sort(A):
    return sorted(enumerate(A),key=itemgetter(1))

N = I()
A = Line(N,1)

B = index_sort(A)
num = 0
for i in range(N):
    if abs(B[i][0]-i)%2==1:
        num += 1

print(num//2)