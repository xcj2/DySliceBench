#import sys
MOD = 10 ** 9 + 7
INFI = 10**10
#input = sys.stdin.readline
import math
from collections import deque
import itertools
import heapq
#import bisect
from fractions import Fraction
import copy
from functools import lru_cache
from collections import defaultdict
import pprint

#oo=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# ko=list("abcdefghijklmnopqrstuvwxyz")

def sosuhante(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n% k ==0:
            return False
    return True
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def kingaku(a,b,n):
    keta=len(str(n))
    return a*n+b*keta

def my_index(l, x, default=False):
    if x in l:
        return l.index(x)
    else:
        return default

#    h,w,a,b = map(int, input().split())
#    c = [[0 for j in range(n)] for i in range(n)]

def ret(a):
    c=[None]*(len(a)-1)
    if len(a)==1:
        return a[0]
    elif len(a)==0:
        return 0
    for i in range(1,len(a)):
        c[i-1]=abs(a[i]-a[i-1])
    return ret(c)

def soinsubunkai(n):
    a = []
    i = 1
    while i*i <= n:
        if n % i == 0 and i!=1:
            a.append(i)
            n=n//i

        if n% i !=0 or i==1:
            i += 1
    nokori=[n]
    return a + nokori

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def main():
    #l,r,d=map(int,input().split())
    h,w= map(int, input().split())
    cx,cy = map(int, input().split())
    dx,dy = map(int, input().split())
    s=[]
    s.append(list("#"*(w+4)))
    s.append(list("#"*(w+4)))
    for i in range(h):
        temp=input()
        temp="##"+temp+"##"
        s.append(list(temp))
    s.append(list("#"*(w+4)))
    s.append(list("#"*(w+4)))
#    for i in range(h+4):
#        print(s[i])

    visited = [[0 for i in range(w+4)] for _ in range(h+4)]
    warpvisited = [[0 for i in range(w + 4)] for _ in range(h + 4)]
    warp = [[INFI for i in range(w+4)] for _ in range(h+4)]
    visited[cx+1][cy+1]=1
    warp[cx+1][cy+1]=0

    queue = deque([])

    warpdire=[[-2,-2],[-1,-2],[0,-2],[1,-2],[2,-2],
           [-2,-1],[-1,-1],[1,-1],[2,-1],
           [-2,0],[2,0],
           [-2,1],[-1,1],[1,1],[2,1],
           [-2,2],[-1,2],[0,2],[1,2],[2,2],
              [0,-1],[-1,0],[1,0],[0,1]]
    walkdire=[[0,-1],[-1,0],[1,0],[0,1]]

    warpvisited = [[0 for i in range(w + 4)] for _ in range(h + 4)]
    walkvisited = [[0 for i in range(w + 4)] for _ in range(h + 4)]
    rekkyo=[]
    rekkyo2=[]
    nowx = cx + 1
    nowy = cy + 1
    def walkloop(nowx,nowy):
        walkvisited[nowx][nowy]=1
        rekkyo.append([nowx,nowy])
        for i in walkdire:
            if s[nowx + i[0]][nowy + i[1]] == "." and walkvisited[nowx + i[0]][nowy + i[1]] == 0:
                queue.append([nowx + i[0], nowy + i[1]])
                warp[nowx + i[0]][nowy + i[1]] = min(warp[nowx][nowy], warp[nowx + i[0]][nowy + i[1]])
                visited[nowx + i[0]][nowy + i[1]] = 1
                walkvisited[nowx + i[0]][nowy + i[1]] = 1
                rekkyo.append([nowx+i[0],nowy+i[1]])
        while queue:
            if len(queue) <= 0:
                return
            now = queue.popleft()
            nowx = now[0]
            nowy = now[1]


            for i in walkdire:
                if s[nowx + i[0]][nowy + i[1]] == "." and walkvisited[nowx + i[0]][nowy + i[1]] == 0:
                    queue.append([nowx + i[0], nowy + i[1]])
                    warp[nowx + i[0]][nowy + i[1]] = min(warp[nowx][nowy], warp[nowx + i[0]][nowy + i[1]])
                    visited[nowx + i[0]][nowy + i[1]] = 1
                    walkvisited[nowx + i[0]][nowy + i[1]] = 1
                    rekkyo.append([nowx + i[0], nowy + i[1]])

        return
    def warploop(nowx,nowy,cost):
        for i in warpdire:
            if s[nowx + i[0]][nowy + i[1]] == "." and warp[nowx + i[0]][nowy + i[1]]>cost:

                warp[nowx + i[0]][nowy + i[1]] = min(warp[nowx][nowy]+1, warp[nowx + i[0]][nowy + i[1]])
                visited[nowx + i[0]][nowy + i[1]] = 1
                warpvisited[nowx + i[0]][nowy + i[1]] = 1
                rekkyo2.append([nowx+i[0],nowy+i[1]])
        return
    cost=0
    walkloop(cx + 1, cy + 1)
    cost += 1

    while True:
        for i in rekkyo:
            warploop(i[0],i[1],cost)
        rekkyo=[]
 #       print(rekkyo2)
        for i in rekkyo2:
            walkloop(i[0],i[1])
        rekkyo2=[]
   #     print(rekkyo)
        if len(rekkyo)==0:
            break

        cost+=1


    if visited[dx+1][dy+1]==0:
        print("-1")
    else:
        print(warp[dx+1][dy+1])

#    for i in range(h+4):
 #       print(visited[i])
 #   for i in range(h+4):
 #      print(warp[i])




if __name__ == "__main__":

    main()
