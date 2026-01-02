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

a = list(input())
b = list(input())
c = list(input())

def is_match(c1,c2):
    if c1 == '?' or c2 == '?' or c1 == c2:
        return True
    else:
        return False

def prefix_match_len(x,y):
    len_list = []
    n = len(x)
    m = len(y)
    for i in range(n):
        match = 0
        for j in range(i,min(i+m,n)):
            if is_match(x[j],y[j-i]):
                match += 1
            else:
                break
        len_list.append(match)
    return len_list

def concat(x,y,xy):
    index_list = []
    n = len(x)
    m = len(y)
    for i in range(n):
        if xy[i] == min(n-i,m):
            index_list.append(i)
    index_list.append(n)
    return index_list

def concat2(x,y,z,xz,yz,zy,index_list):
    n1 = len(x)
    n2 = len(y)
    m = len(z)
    candidate = []
    for i in index_list:
        flag = False
        for j in range(max(n1,n2+i)):
            if j <= n1-1:
                if xz[j] != min(n1-j,m):
                    continue
            if j >= i:
                if n2-j+i >= 1 and yz[j-i] != min(n2-j+i,m):
                    continue
            else:
                if m-i+j >= 1 and zy[i-j] != min(m-i+j,n2):
                    continue
            flag = True
            candidate.append(max(n1,n2+i,j+m))
            break
        if not flag:
            candidate.append(max(n1,n2+i)+m)
    return min(candidate)

ab = prefix_match_len(a,b)
ac = prefix_match_len(a,c)
ba = prefix_match_len(b,a)
bc = prefix_match_len(b,c)
ca = prefix_match_len(c,a)
cb = prefix_match_len(c,b)

index_list = concat(a,b,ab)
ret1 = concat2(a,b,c,ac,bc,cb,index_list)
index_list = concat(a,c,ac)
ret2 = concat2(a,c,b,ab,cb,bc,index_list)
index_list = concat(b,a,ba)
ret3 = concat2(b,a,c,bc,ac,ca,index_list)
index_list = concat(b,c,bc)
ret4 = concat2(b,c,a,ba,ca,ac,index_list)
index_list = concat(c,a,ca)
ret5 = concat2(c,a,b,cb,ab,ba,index_list)
index_list = concat(c,b,cb)
ret6 = concat2(c,b,a,ca,ba,ab,index_list)

print(min(ret1,ret2,ret3,ret4,ret5,ret6))