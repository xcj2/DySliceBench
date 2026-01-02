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
    n = I()
    v = LI()
    even_count = collections.defaultdict(int)
    odd_count = collections.defaultdict(int)
    for i in range(n):
        if i % 2 == 1:
            odd_count[v[i]] += 1
        else:
            even_count[v[i]] += 1
    odd_array = []
    even_array = []
    for k, v in odd_count.items():
        odd_array.append((k, v))
    for k, v in even_count.items():
        even_array.append((k, v))

    odd_array = sorted(odd_array, key=lambda x:x[1])[::-1]
    even_array = sorted(even_array, key=lambda x:x[1])[::-1]

    ans = inf
    arrLen = n // 2
    for ok, ov in odd_array[:2]:
        for ek, ev in even_array[:2]:
            if ok == ek:
                continue
            ans = min(ans, (arrLen - ov) + (arrLen - ev))
    if ans == inf:
        ans = arrLen
    print(ans)
main()

