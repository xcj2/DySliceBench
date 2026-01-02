# -*- coding: utf-8 -*-
"""
AtCoder A
"""

import sys, math, random
import numpy as np
import itertools
from functools import reduce
from itertools import chain
# N = int(input())
# A = list(map(int,input().split())) # N row 1 column
# A = [int(input()) for _ in range(N)] # 1 row N column
# S = str(input()) # str(input()) == input() -> 'abc'
# S = list(input()) # abc -> ['a','b','c']
# S.replace('ABC','X') # "testABCABC" -> "testXX"

inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    N=I()
    X=S()
    OUT=np.array([[[0]*10]*10]*10)

    for i in range(10):
        x=(X.find(str(i)))
        if x>-1:
            X2=X[x+1:]
            for j in range(10):
                y=(X2.find(str(j)))
                if y>-1:
                    X3=X2[y+1:]
                    for k in range(10):
                        z=(X3.find(str(k)))
                        if z>-1:
                            OUT[i][j][k]=1

    print(OUT.sum())


        # for j in range(10):
        #     max_idx=0
        #     for k in range(10):
        #         target=[i,j,k]
        #         idx=0

        #         for x in X:
        #             if x==str(target[idx]):
        #                 idx+=1
        #             if idx==3:
        #                 OUT[i][j][k]=1
        #                 max_idx=idx
        #                 break
        #         max_idx=idx
        #         if max_idx<2:
        #             break



    # print(OUT.sum())
    # print(sum(list(chain.from_iterable(OUT))))

if __name__ == "__main__":
    main()


#     # -*- coding: utf-8 -*-
# """
# AtCoder A
# """

# import sys, math, random
# # import numpy as np
# import itertools
# from functools import reduce
# # N = int(input())
# # A = list(map(int,input().split())) # N row 1 column
# # A = [int(input()) for _ in range(N)] # 1 row N column
# # S = str(input()) # str(input()) == input() -> 'abc'
# # S = list(input()) # abc -> ['a','b','c']
# # S.replace('ABC','X') # "testABCABC" -> "testXX"

# inf = 10**20
# eps = 1.0 / 10**10
# mod = 10**9+7
# dd = [(-1,0),(0,1),(1,0),(0,-1)]
# ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# def LI(): return list(map(int, sys.stdin.readline().split()))
# def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
# def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
# def LS(): return sys.stdin.readline().split()
# def I(): return int(sys.stdin.readline())
# def F(): return float(sys.stdin.readline())
# def S(): return input()


# def main():
#     N=I()
#     X=S()
#     OUT=np.array([[[0]*10]*10]*10)
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 target=[i,j,k]
#                 idx=0
#                 for x in X:
#                     if x==str(target[idx]):
#                         idx+=1
#                     if idx==3:
#                         OUT[i][j][k]=1
#                         break
#     print(OUT.sum())
#     sum(reduce(lambda a, b: a + b, OUT))

# if __name__ == "__main__":
#     main()