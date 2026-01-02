#!/usr/bin/env python3
#dp3 #Vacation
import sys
def S(): return list(sys.stdin.readline())[:-1]
def LI(): return list(map(int,sys.stdin.readline().split()))
def c():
    n = int(input())
    dpa = [0]*n
    dpb = [0]*n
    dpc = [0]*n

    a,b,c = LI()
    dpa[0] = a
    dpb[0] = b
    dpc[0] = c
    for i in range(1,n):
        a,b,c = LI()
        dpa[i] = max(dpb[i-1] + a,dpc[i-1] + a)
        dpb[i] = max(dpa[i-1] + b,dpc[i-1] + b)
        dpc[i] = max(dpa[i-1] + c,dpb[i-1] + c)
    print(max(dpa[-1],dpb[-1],dpc[-1]))
if __name__ == '__main__':
    c()
