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

T1,T2 = LI()
A1,A2 = LI()
B1,B2 = LI()

if A1 > B1 and A2 > B2:
    print(0)
    exit()
if A1 < B1 and A2 < B2:
    print(0)
    exit()

if A1 > B1:
    t = (A1-B1)*T1 / (B2-A2)
    delta = (A1-B1)*T1+(A2-B2)*T2
    if t == T2:
        print('infinity')
        exit()
    elif t > T2:
        print(0)
        exit()
    else:
        if delta > 0:
            print(math.floor((T2-t)*(B2-A2)/delta) + 1)
            exit()
        else:
            x = (A1-B1)*T1 / (-delta)
            if int(x) == x:
                print(2*int(x))
            else:
                print(2*math.floor(x)+1)

else:
    t = (B1-A1)*T1 / (A2-B2)
    delta = (B1-A1)*T1+(B2-A2)*T2
    if t == T2:
        print('infinity')
        exit()
    elif t > T2:
        print(0)
        exit()
    else:
        if delta > 0:
            print(math.floor((T2-t)*(A2-B2)/delta) + 1)
            exit()
        else:
            x = (B1-A1)*T1 / (-delta)
            if int(x) == x:
                print(2*int(x))
            else:
                print(2*math.floor(x)+1)