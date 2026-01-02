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

# 適当に根を決める
# 根から偶数回でも奇数回でも行ける点があれば，結局全部繋げる
# なければ，偶奇が異なるものだけ繋げる

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if not directed:
            pt[t[i]-1].append(s[i]-1)
    return pt

N,M = LI()
A,B = LIR(M,2)

pt = edges_to_pt(A,B,N)

odd = [False]*N
even = [False]*N
even[0] = True

q = [0]
c = 1
flag = False
while q:
    q1 = []
    for v in q:
        for u in pt[v]:
            if c%2:
                if even[u]:
                    flag = True
                    break
                if not odd[u]:
                    odd[u] = True
                    q1.append(u)
            else:
                if odd[u]:
                    flag = True
                    break
                if not even[u]:
                    even[u] = True
                    q1.append(u)                
        if flag:
            break
    if flag:
        break
    q = q1
    c += 1

if flag:
    print(N*(N-1)//2 - M)
else:
    odds = 0
    evens = 0
    for i in range(N):
        if odd[i]:
            odds += 1
        else:
            evens += 1
    print(odds*evens - M)