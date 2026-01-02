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

N,A,B = II()

if (A-B)%2==0:
    print(abs((A-B)//2))
else:
    a = min(A,B)
    b = max(A,B)
    n1 = a + (b-a-1)//2
    n2 = (N-b+1) + (b-a-1)//2
    print(min(n1,n2))