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

N,A,B,C = LI()
s = ['0']*N
for i in range(N):
    s[i] = str(input())

d = defaultdict(int)
d['A'] = A
d['B'] = B
d['C'] = C

def plus_minus(s,t):
    for c in ['A','B','C']:
        if (c in s) and (c in t):
            plus = c
    if s[0] == plus:
        minus = s[1]
    else:
        minus = s[0]
    return plus, minus 

def min_max(s):
    if d[s[0]] >= d[s[1]]:
        return s[1],s[0]
    else:
        return s[0],s[1]

if A+B+C == 0:
    print('No')
elif A+B+C == 1:
    ans = []
    for i in range(N):
        if d[s[i][0]] == d[s[i][1]] == 0:
            print('No')
            exit()
        else:
            if d[s[i][0]]:
                d[s[i][0]] -= 1
                d[s[i][1]] += 1
                ans.append(s[i][1])
            else:
                d[s[i][1]] -= 1
                d[s[i][0]] += 1
                ans.append(s[i][0])
    print('Yes')
    for a in ans:
        print(a)
else:
    if d[s[0][0]] == d[s[0][1]] == 0:
        print('No')
    else:
        print('Yes')
        for i in range(N):
            if d[s[i][0]] == 0:
                d[s[i][0]] += 1
                d[s[i][1]] -= 1
                print(s[i][0])
            elif d[s[i][1]] == 0:
                d[s[i][1]] += 1
                d[s[i][0]] -= 1
                print(s[i][1])
            elif d[s[i][0]] == d[s[i][1]] == 1:
                if i != N-1:
                    p,m = plus_minus(s[i],s[i+1])
                    d[p] += 1
                    d[m] -= 1
                    print(p)
                else:
                    d[s[i][0]] += 1
                    d[s[i][1]] -= 1
                    print(s[i][0])
            else:
                min_,max_ = min_max(s[i])
                d[min_] += 1
                d[max_] -= 1
                print(min_)