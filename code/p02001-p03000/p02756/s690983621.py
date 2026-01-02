import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
from collections import Counter,defaultdict,deque
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    s = str(input())
    q = inp()
    before = []
    after = []
    flag = True
    for _ in range(q):
        query = inpls()
        if query[0] == '1':
            if flag:
                flag = False
            else:
                flag = True
        else:
            f = query[1]
            S = query[2]
            if (flag and f=='2') or ((not flag) and f=='1'):
                after.append(S)
            else:
                before.append(S)
    ans = []
    for i in range(len(before)-1,-1,-1):
        ans.append(before[i])
    s = list(s)
    for i in range(len(s)):
        ans.append(s[i])
    for i in range(len(after)):
        ans.append(after[i])
    if not flag:
        ans.reverse()
    print(''.join(ans))
    
if __name__ == "__main__":
    main()