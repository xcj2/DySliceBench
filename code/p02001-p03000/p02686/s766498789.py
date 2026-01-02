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
S = []
for i in range(N):
    S.append(list(input()))

# 最終的な '(' - ')' の数
diff = [0]*N
for i in range(N):
    num = 0
    for j in range(len(S[i])):
        if S[i][j] == '(':
            num += 1
        else:
            num -= 1
    diff[i] = num

if sum(diff) != 0:
    print('No')
    exit()

# 条件が最も厳しい場所での括弧の数の差
bottom = [0]*N
for i in range(N):
    if diff[i] >= 0:
        num = 1 if S[i][0] == ')' else -1
        val = num
        for j in range(1,len(S[i])):
            if S[i][j] == '(':
                num -= 1
            else:
                num += 1
                val = max(val,num)
        bottom[i] = val
    else:
        num = 1 if S[i][-1] == '(' else -1
        val = num
        for j in range(1,len(S[i]))[::-1]:
            if S[i][j] == ')':
                num -= 1
            else:
                num += 1
                val = max(val,num)
        bottom[i] = val
    
up = []
down = []
for i in range(N):
    if diff[i] >= 0:
        up.append((diff[i],bottom[i]))
    else:
        down.append((diff[i],bottom[i]))

up.sort(key=lambda x: x[1])
down.sort(key=lambda x: -x[1])

r = 0
for u in up:
    if r < u[1]:
        print('No')
        exit()
    else:
        r += u[0]

r = 0
for d in down[::-1]:
    if r < d[1]:
        print('No')
        exit()
    else:
        r += -d[0]

print('Yes')