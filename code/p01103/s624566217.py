import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2,gcd
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()


def INT(): return int(input())


def MAP(): return map(int, input().split())


def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

def main():

    ans=[]
    
    while 1:
        d,w = MAP()

        if d==0 and w == 0:
            break
        else:
            lis=[]

            e=[LIST() for _ in range(d) ]

            #print(d,w)

            for x in combinations(range(d),2):
                for y in combinations(range(w),2):
                    if x[1]-x[0]!=1 and y[1]-y[0]!=1:

                        waku_min=9
                        naka_max=0
                        a=0
                        for p in range(x[0],x[1]+1):
                            for q in range(y[0],y[1]+1):
                                if p == x[0] or p == x[1] or q == y[0] or q == y[1] :
                                    waku_min=min(waku_min,e[p][q])
                                else:
                                    naka_max=max(naka_max,e[p][q])

                        if waku_min > naka_max:
                            #print('tate:',x)
                            #print('yoko:',y)
                            #print(waku_min,naka_max)
                            for p in range(x[0]+1,x[1]):
                                for q in range(y[0]+1,y[1]):
                                    a += waku_min-e[p][q]

                            lis.append(a)

            if not lis:
                ans.append(0)
            else:
                ans.append(max(lis))

        #print('lis:' ,lis)

    for x in ans:
        print(x)




if __name__ == '__main__':
    main()

