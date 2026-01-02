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

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed == False:
            pt[t[i]-1].append(s[i]-1)
    return pt

def bfs(pt,s):
    n = len(pt)
    d = [-1]*n
    d[s] = 0
    q = [s]
    c = 1
    while q:
        q1 = []
        for v in q:
            for u in pt[v]:
                if d[u] == -1:
                    d[u] = c
                    q1.append(u)
        q = q1
        c += 1
    return d

N = I()
a,b = LIR(N-1,2)

if N%3 == 0:
    one_num,two_num,zero_num = N//3,N//3,N//3
elif N%3 == 1:
    one_num,two_num,zero_num = N//3+1,N//3,N//3
else:
    one_num,two_num,zero_num = N//3+1,N//3+1,N//3

pt = edges_to_pt(a,b,N)
d = bfs(pt,0)

# 根からの距離の偶奇で群分け
odd = []
even = []
for i in range(N):
    if d[i]%2 == 0:
        even.append(i)
    else:
        odd.append(i)

max_ = max(len(even),len(odd))
min_ = min(len(even),len(odd))
if max_ == len(even):
    max_index = even
    min_index = odd
else:
    max_index = odd
    min_index = even

ans = [0]*N

# 各群の個数が十分多ければ，1と2を各群に振り分ける
if max_ >= one_num and min_ >= two_num:
    for i in range(one_num):
        ans[max_index[i]] = 1
    for i in range(two_num):
        ans[min_index[i]] = 2
# 片側の群の個数が少なければ，そちらに0を固める
else:
    for i in range(one_num):
        ans[max_index[i]] = 1
    for i in range(one_num,one_num+two_num):
        ans[max_index[i]] = 2

one_p = 0
two_p = 0
zero_p = 1
for i in range(N):
    if ans[i] == 1:
        ans[i] = 3*one_p+1
        one_p += 1
    elif ans[i] == 2:
        ans[i] = 3*two_p+2
        two_p += 1
    else:
        ans[i] = 3*zero_p
        zero_p += 1

print(*ans)