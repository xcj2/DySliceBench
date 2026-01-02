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

def ceil(a,b):
    return a//b + int(a%b != 0)

N,H = LI()
a,b = LIR(N,2)

x = []
for i in range(N):
    x.append((a[i],0))
    x.append((b[i],1))

x.sort(key=lambda x: (-x[0],x[1]))

val = 0
count = 0
for x0 in x:
    if x0[1] == 0:
        use_a = x0[0]
        break
    else:
        val += x0[0]
        count += 1
        if val >= H:
            print(count)
            exit()

H -= val
ans = count + ceil(H,use_a)
print(ans)