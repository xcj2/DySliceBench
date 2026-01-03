from collections import deque
from heapq import heapify,heappop,heappush,heappushpop
from copy import copy,deepcopy
from itertools import permutations,combinations
from pprint import pprint

def myinput():
    return map(int,input().split())

def mycol(data,col):
    return [ row[col] for row in data ]

def mysort(data,col):
    data.sort(key=lambda x:x[col],reverse=False)
    return data

def mymax(data):
    M = -1*float("inf")
    for i in range(len(data)):
        m = max(data[i])
        M = max(M,m)
    return M

def mymin(data):
    m = float("inf")
    for i in range(len(data)):
        M = min(data[i])
        m = min(m,M)
    return m

# ----- heapq ここから-----
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
        if self.desc: self.hq[0].val
        else: return self.hq[0]
# ----- heapq ここまで-----

n = int(input())
a = list(myinput())
# print(a)

red = a[:n]
blue = a[(2*n):]

s_red = sum(red)
s_blue = sum(blue)

ans = s_red - s_blue
# print(ans)

hq_red = Heapq(red,False)
# print(red)
hq_blue = Heapq(blue,True)
# print(blue)

ans = -1*float("inf")

ls_s_red = [s_red]
for k in range(n,2*n):
    hq_red.push(a[k])
    p = hq_red.pop()
    s_red = s_red + a[k] - p  
    ls_s_red.append(s_red)
# print(ls_s_red)   

ls_s_blue = [s_blue]
for k in range(n,2*n):
    hq_blue.push(a[-(k+1)])
    p = hq_blue.pop()
    s_blue = s_blue + a[-(k+1)] - p
    ls_s_blue.append(s_blue)
ls_s_blue_sorted = ls_s_blue[::-1]
# print(ls_s_blue_sorted)

for k in range(len(ls_s_red)):
    M = ls_s_red[k] - ls_s_blue_sorted[k]
    ans = max(ans,M)

print(ans)