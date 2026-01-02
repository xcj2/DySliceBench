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
     
nums = ['3', '5', '7']
cnt = 0

def dfs(cur, s):
    global cnt
    if len(cur) > 0 and '3' in cur and '5' in cur and '7' in cur:
        cnt += 1
    for c in nums:
        cur.append(c)
        if int(''.join(cur)) > int(s):
            return
        newcur = cur.copy()
        dfs(newcur, s)
        cur.pop()

def main():
    s = S()
    N = len(s)
    cur = []
    dfs(cur, s)
    print(cnt)

main()

