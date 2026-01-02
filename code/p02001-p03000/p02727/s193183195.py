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

# heapq
import heapq
class Reverse:
    def __init__(self, val):
        self.val = val
        
    def __lt__(self, other):
        return self.val > other.val
        
    def __repr__(self):
        return repr(self.val)
    
class Heapq:
    def __init__(self, arr, desc = False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        if self.desc: return heapq.heappop(self.hq).val
        else: return heapq.heappop(self.hq)
 
    def push(self, a):
        if self.desc: heapq.heappush(self.hq, Reverse(a))
        else: heapq.heappush(self.hq, a)
 
    def top(self):
        if self.desc: return self.hq[0].val
        else: return self.hq[0]

from operator import itemgetter
def index_sort(A):
    A_sort = sorted(enumerate(A),key=itemgetter(1))
    index = [a[0] for a in A_sort]
    sorted_A = [a[1] for a in A_sort]
    return index, sorted_A

X,Y,A,B,C = LI()
p = LI()
q = LI()
r = LI()

Z = []
for i in range(A):
    Z.append((p[i],0)) # red
for i in range(B):
    Z.append((q[i],1)) # green
for i in range(C):
    Z.append((r[i],2))

Z.sort(key=lambda x:(-x[0],-x[1]))
index = [Z[i][1] for i in range(len(Z))]

R = []
G = []
M = []
Rm = Heapq([])
Gm = Heapq([])
ans = 0

for i in range(X+Y):
    ans += Z[i][0]
    if Z[i][1] == 0:
        R.append(Z[i][0])
        Rm.push(Z[i][0])
    elif Z[i][1] == 1:
        G.append(Z[i][0])
        Gm.push(Z[i][0])
    else:
        M.append(Z[i][0])
        #Rm.push(Z[i][0])
        #Gm.push(Z[i][0])

nr = len(R)
ng = len(G)
nm = len(M)
for i in range(X+Y,A+B+C):
    if ng+nm < Y:
        if Z[i][1] == 0:
            continue
        else:
            v = Rm.pop()
            #Gm.push(Z[i][0])
            ng += 1
            nr -= 1
            ans -= v
            ans += Z[i][0]
    elif nr+nm < X:
        if Z[i][1] == 1:
            continue
        else:
            v = Gm.pop()
            #Rm.push(Z[i][0])
            nr += 1
            ng -= 1
            ans -= v
            ans += Z[i][0]
    else:
        break

print(ans)