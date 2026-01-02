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
    d = collections.OrderedDict()
    A = sorted(A)[::-1]
    for a in A:
        if not a in d:
            d[a] = 1
        else:
            d[a] += 1
    l_num = -1
    ans = 0
    for num, freq in d.items():
        if freq < 2:
            continue
        else:
            if l_num == -1:
                l_num = num
            else:
                ans = l_num * num
                break
        if freq >= 4:
            ans = num * num
            break
    print(ans)
main()

