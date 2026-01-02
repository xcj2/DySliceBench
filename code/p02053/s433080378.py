#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    h,w = LI()
    s = SR(h)
    ans = 1
    for y in range(h):
        for x in range(w):
            if s[y][x] == "B":
                for y_ in range(h):
                    for x_ in range(w):
                        if s[y_][x_] == "B":
                            ans = max(ans, abs(y-y_)+abs(x-x_))
    print(ans)
    return

#B
def B():

    def quickhull(l,r,s,k,il,ir):
        if not s:
            return
        su = []
        sd = []
        a = (r[0]-l[0],r[1]-l[1])
        for x,y in s:
            b = (x-l[0],y-l[1])
            cro = cross(a,b)
            if cro > 0:
                su.append((x,y)) #上半分
            elif cro < 0:
                sd.append((x,y)) #下半分

        ind = (ir-il)/2 #凸包に追加する頂点が反時計回りで何番目かを表す基数

        if su:
            c,d = direction(l,r,su[0])
            p = su[0]
            for i in range(1,len(su)):
                c_,d_ = direction(l,r,su[i])
                if c*d_ < c_*d:
                    c,d = c_,d_
                    p = su[i]
            i = ir+ind #irよりも後
            k.append((tuple(p),i)) #もっとも離れた点を凸包の頂点に追加
            b = (l[0]-p[0],l[1]-p[1])
            c = (p[0]-r[0],p[1]-r[1])
            s1 = []
            s2 = []
            for x,y in su:
                b_ = (x-p[0],y-p[1])
                c_ = (x-r[0],y-r[1])
                cro_b,cro_c = cross(b,b_),cross(c,c_)
                if cro_b >= 0 and cro_c >= 0: #三角形内部判定
                    continue
                else:
                    if cro_b < 0:
                        s1.append((x,y))
                    elif cro_c < 0:
                        s2.append((x,y))
            quickhull(l,p,s1,k,il,i) #再帰
            quickhull(r,p,s2,k,ir,i) #順序がr->pの点に注意して再帰

        if sd:
            c,d = direction(l,r,sd[0])
            p = sd[0]
            for i in range(1,len(sd)):
                c_,d_ = direction(l,r,sd[i])
                if c*d_ < c_*d:
                    c,d = c_,d_
                    p = sd[i]
            i = il+ind
            k.append((tuple(p),i)) #もっとも離れた点を凸包の頂点に追加
            b = (l[0]-p[0],l[1]-p[1])
            c = (p[0]-r[0],p[1]-r[1])
            s1 = []
            s2 = []
            for x,y in sd:
                b_ = (x-p[0],y-p[1])
                c_ = (x-r[0],y-r[1])
                cro_b,cro_c = cross(b,b_),cross(c,c_)
                if cro_b <= 0 and cro_c <= 0: #三角形内部判定(ベクトルの向きにより上下で判定が異なることに注意)
                    continue
                else:
                    if cro_b > 0:
                        s1.append((x,y))
                    elif cro_c > 0:
                        s2.append((x,y))
            quickhull(l,p,s1,k,il,i) #再帰
            quickhull(p,r,s2,k,i,ir) #順序がp->rの点に注意して再帰
        k.sort(key = lambda x:x[1])
        return tuple(zip(*k))[0]

    def cross(a,b): #外積
        return a[0]*b[1]-a[1]*b[0]

    def direction(l,r,p): #点と直線の距離
        a = r[1]-l[1]
        b = l[0]-r[0]
        return (a*(p[0]-l[0])+b*(p[1]-l[1]))**2, a**2+b**2 #分子の2乗,分母の2乗

    def manh(x,y):
        return abs(x[0]-y[0])+abs(x[1]-y[1])
    h,w = LI()
    c = SR(h)
    s = []
    for y in range(h):
        for x in range(w):
            if c[y][x] == "B":
                s.append([x,y])
    n = len(s)
    if n < 1000:
        ans = 1
        for x in s:
            for y in s:
                ans = max(ans,manh(x,y))
        print(ans)
    else:
        s.sort()
        l = tuple(s.pop(0))
        r = tuple(s.pop(-1))
        k = quickhull(l,r,s,[(l,0),(r,n)],0,n)
        ans = 1
        for x in k:
            for y in k:
                ans = max(ans,manh(x,y))
        print(ans)
    return

#C
def C():
    n = I()

    return

#D
def D():
    n = I()

    return

#E
def E():
    n = I()

    return

#F
def F():
    n = I()

    return

#G
def G():
    n = I()

    return

#H
def H():
    n = I()

    return

#I
def I_():
    n = I()

    return

#J
def J():
    n = I()

    return

#Solve
if __name__ == "__main__":
    B()

