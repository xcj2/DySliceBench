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
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

N = I()

count = 0
d = defaultdict(int)
for i in range(1,10):
    for j in range(1,10):
        count = 0
        for k in range(1,N+1):
            if str(k)[0]==str(j) and str(k)[-1]==str(i):
                count += 1
        d[(i,j)] = count
#print(d)

ans = 0
for i in range(1,N+1):
    ans += d[(int(str(i)[0]),int(str(i)[-1]))]
    #print(i,d[(int(str(i)[0]),int(str(i)[-1]))])
print(ans)