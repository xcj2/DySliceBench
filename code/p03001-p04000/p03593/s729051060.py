import sys
import math
from collections import defaultdict

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
a  = [list(map(str,input())) for _ in range(H)]

d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[a[i][j]] += 1

if H%2 == 0 and W%2 == 0:
    for k in d.keys():
        if d[k]%4 != 0:
            print('No')
            exit()
    print('Yes')
elif H%2 == 0 and W%2 != 0:
    count = 0
    for k in d.keys():
        if d[k]%4 != 0:
            if d[k]%2 != 0:
                print('No')
                exit()
            else:
                count += 1
    if count%2 == (H//2)%2 and H//2 >= count:
        print('Yes')
    else:
        print('No')
elif W%2 == 0 and H%2 != 0:
    count = 0
    for k in d.keys():
        if d[k]%4 != 0:
            if d[k]%2 != 0:
                print('No')
                exit()
            else:
                count += 1
    if count%2 == (W//2)%2 and W//2 >= count:
        print('Yes')
    else:
        print('No')
else:
    odd_flag = False
    count = 0
    for k in d.keys():
        if d[k]%4 != 0:
            if d[k]%2 != 0:
                if not odd_flag:
                    odd_flag = True
                    if (d[k]-1)%4 != 0:
                        count += 1
                else:
                    print('No')
                    exit()
            else:
                count += 1
    if count%2 == ((H-1)//2+(W-1)//2)%2 and (H-1)//2+(W-1)//2 >= count:
        print('Yes')
    else:
        print('No')