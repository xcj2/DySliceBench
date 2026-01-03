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
    q = deque()
    N = I()
    s = S()
    cnt_l = 0 # (
    cnt_r = 0 # )

    for c in s:
        if c == '(':
            cnt_l += 1
        else:
            cnt_r += 1
            if cnt_l > 0:
                cnt_l -= 1
                cnt_r -= 1
        q.append(c)
    while cnt_l:
        q.append(')')
        cnt_l -= 1
    while cnt_r:
        q.appendleft('(')
        cnt_r -= 1
    ans = []
    for c in q:
        ans.append(c)
    print(''.join(ans))

main()

