import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    strings = []
    prevdic = None
    for _ in range(N):
        ch = S()
        curdic = collections.Counter()
        for c in ch:
            curdic[c] += 1
        if prevdic:
            for k, v in prevdic.items():
                prevdic[k] = min(v, curdic[k])
        else:
            prevdic = curdic
    diclist = []
    for k, v in prevdic.items():
        diclist.append((k, v))
    diclist = sorted(diclist, key=lambda x: x[0])
    ans = ''
    for item in diclist:
        k, v = item[0], item[1]
        ans += k * v
    print(ans)
main()

