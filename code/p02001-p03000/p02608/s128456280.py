from math import *
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
for x in range(1,n+1):
    ans = 0
    m = ceil(sqrt(x))+1
    for i in range(1, m):
        for j in range(i, m):
            tmp = (i+j)**2 - 4*(i**2+j**2+i*j-x)
            if tmp > (i+j)**2:
                k = ( -(i+j) + sqrt(tmp) ) // 2
                if k >= j and i**2 + j**2 + k**2 + i*j + j*k + k*i == x:
                    if i == j == k:
                        ans += 1
                    elif i == j or j == k or k == i:
                        ans += 3
                    else:
                        ans += 6
    print(ans)