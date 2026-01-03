import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    a = set([1,3,5,7,8,10,12])
    b = set([4,6,9,11])
    c = set([2])
    x,y = LI()
    d = [a,b,c]
    xi = yi = -1
    for i in range(3):
        if x in d[i]:
            xi = i
        if y in d[i]:
            yi = i

    if xi == yi:
        return 'Yes'

    return 'No'



print(main())
