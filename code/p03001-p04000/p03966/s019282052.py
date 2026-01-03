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

def next_mul(x,y):
    if x%y == 0:
        return x
    else:
        return x+y-x%y

N = I()
T,A = LIR(N,2)

t = T[0]
a = A[0]
for i in range(1,N):
    an = next_mul(a,A[i])
    tn = an*T[i]//A[i]
    if tn >= t:
        t = tn
        a = an
    else:
        t = next_mul(t,T[i])
        a = t*A[i]//T[i]
        
print(t+a)