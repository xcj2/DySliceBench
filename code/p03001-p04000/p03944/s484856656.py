import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return list(map(int, input().split()))
def II(): return int(input())
def S(): return input()


def main():
    w,h,n = LI()
    a = [[1]*w for _ in range(h)]
    for _ in range(n):
        x,y,t = LI()
        if t == 1:
            for _x in range(x):
                for _y in range(h):
                    a[_y][_x] = 0
        elif t == 2:
            for _x in range(x, w):
                for _y in range(h):
                    a[_y][_x] = 0
        elif t == 3:
            for _x in range(w):
                for _y in range(y):
                    a[_y][_x] = 0
        else:
            for _x in range(w):
                for _y in range(y,h):
                    a[_y][_x] = 0
    return sum(sum(_) for _ in a)





print(main())
