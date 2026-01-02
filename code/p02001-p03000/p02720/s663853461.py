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
     
num = []
def dfs(n, curnum):
    if n == 0:
        num.append(curnum)
        return
    last = int(curnum[-1])
    next_digits = []
    for k in [-1, 0, 1]:
        if 9 >= last + k >= 0:
            next_digits.append(str(last + k))
    for dig in next_digits:
        dfs(n-1, curnum + dig)

def main():
    K = I()
    for i in range(0, 100):
        for j in range(1, 10):
            dfs(i, str(j))
            if len(num) > K:
                print(num[K-1])
                return


main()

