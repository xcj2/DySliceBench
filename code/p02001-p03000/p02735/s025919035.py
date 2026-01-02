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

H,W = LI()
S = [list(map(str, input())) for _ in range(H)]

count = [[0]*W for _ in range(H)]
for i in range(H)[::-1]:
    for j in range(W)[::-1]:
        if i==H-1 and j==W-1:
            if S[i][j] == '#':
                count[i][j] = 1
            else:
                count[i][j] = 0
        elif i==H-1:
            if S[i][j+1]=='.' and S[i][j]=='#':
                count[i][j] = count[i][j+1]+1
            else:
                count[i][j] = count[i][j+1]
        elif j==W-1:
            if S[i+1][j]=='.' and S[i][j]=='#':
                count[i][j] = count[i+1][j]+1
            else:
                count[i][j] = count[i+1][j]
        else:
            if S[i][j+1]=='.' and S[i][j]=='#':
                one = count[i][j+1]+1
            else:
                one = count[i][j+1]
            if S[i+1][j]=='.' and S[i][j]=='#':
                two = count[i+1][j]+1
            else:
                two = count[i+1][j]
            count[i][j] = min(one,two)

print(count[0][0])