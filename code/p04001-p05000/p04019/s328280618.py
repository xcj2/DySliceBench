def examA():
    S = SI()
    d = defaultdict(bool)
    ans = "Yes"
    for s in S:
        d[s] = True
    if (d["S"] and (not d["N"])) or (d["N"] and (not d["S"])):
        ans = "No"
    if (d["E"] and (not d["W"])) or (d["W"] and (not d["E"])):
        ans = "No"
    print(ans)


import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examA()
