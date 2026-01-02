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

S = str(input())

if S=='SUN':
    print(7)
elif S=='MON':
    print(6)
elif S=='TUE':
    print(5)
elif S=='WED':
    print(4)
elif S=='THU':
    print(3)
elif S=='FRI':
    print(2)
elif S=='SAT':
    print(1)
else:
    pass