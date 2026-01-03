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
    A = LI()
    dic = collections.Counter()
    for a in A:
        dic[a] += 1
    even = False
    if N % 2 == 0:
        even = True
    cnt = 1
    n_element = 0
    if not even:
        for key, val in dic.items():
            if key == 0:
                continue
            if key % 2 > 0:
                cnt = 0
                break
            if val != 2:
                cnt = 0
                break
            n_element += 1

        for i in range(n_element):
            cnt = cnt * 2 % mod
        if dic[0] != 1:
            cnt = 0
    else:
        for key, val in dic.items():
            if key % 2 == 0:
                cnt = 0
                break
            if val != 2:
                cnt = 0
                break
            n_element += 1

        for i in range(n_element):
            cnt = cnt * 2 % mod
    print(cnt)

main()

