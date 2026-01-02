# import bisect
# from collections import Counter, deque
# import copy
# from fractions import gcd
# from functools import reduce
# from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline

def resolve():
    N=int(input())
    data=[list(map(int,input().split())) for i in range(N)]
    data=sorted(data,key=lambda x: x[2], reverse=True)

    def height(X,Y,Cx,Cy,H):
        return max(H-abs(X-Cx)-abs(Y-Cy),0)
    def main():
        for i in range(101):
            for j in range(101):
                H = data[0][2] + abs(data[0][0] - i) + abs(data[0][1] - j)
                for k in range(1,N):
                    if height(data[k][0],data[k][1],i,j,H)!=data[k][2]:
                        break
                    elif k==N-1:
                        print(i,j,H)
                        return None

    main()

resolve()