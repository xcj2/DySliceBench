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

#heapq
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


N,C = II()
s,t,c = Line(N,3)

# 同じチャンネルで，空き時間なしで番組が続くときはまとめて録画する
new_s = []
new_t = []
tl = [[] for _ in range(C)]
for i in range(N):
    tl[c[i]-1].append((s[i],t[i]))
for j in range(C):
    if not tl[j]:
        continue
    tl[j].sort(key=itemgetter(0))
    sj = []
    tj = []
    start,last = tl[j][0][0],tl[j][0][1]
    for i in range(1,len(tl[j])):
        if tl[j][i][0] != last:
            sj.append(start)
            tj.append(last)
            start = tl[j][i][0]
            last = tl[j][i][1]
        else:
            last = tl[j][i][1]
    sj.append(start)
    tj.append(last)
    new_s.extend(sj)
    new_t.extend(tj)

index, _ = index_sort(new_s)
s = [new_s[i] for i in index]
t = [new_t[i] for i in index]

h = Heapq([10**6])
ans = 0
for i in range(len(s)):
    if h.top() < s[i]:
        h.pop()
        h.push(t[i])
    else:
        h.push(t[i])
        ans += 1

print(ans)