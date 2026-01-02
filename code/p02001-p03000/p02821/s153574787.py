import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N,num):
    if N<=0:
        return [[] for _ in range(num)]
    elif num==1:
        return [I() for _ in range(N)]
    else:
        read_all = [tuple(II()) for _ in range(N)]
        return map(list, zip(*read_all))

#################

import cmath
pi = cmath.pi
exp = cmath.exp

def convolution(a,b):
    
    def fft(a,sz,inv=False):
        tmp = [0]*sz
        mask = sz-1
        p = 0
        i = sz>>1
        sign = 1 if inv else -1

        while i:
            if p&1:
                cur,nex = tmp,a
            else:
                cur,nex = a,tmp
            ei = exp(2j*pi*i*sign/sz)
            w = 1
            for j in range(0,sz,i):
                for k in range(i):
                    nex[j+k] = cur[((j<<1)&mask)+k] + w*cur[(((j<<1)+i)&mask)+k]
                w *= ei
            p += 1
            i >>= 1

        if p&1:
            a,tmp = tmp,a
        if inv:
            a = list(map(lambda x: x/sz, a))
        return a
    
    sz = 1<<(len(a)+len(b)-2).bit_length()
    a = a + [0]*(sz-len(a))
    b = b + [0]*(sz-len(b))

    fa = fft(a,sz)
    fb = fft(b,sz)
    fafb = [fai*fbi for fai,fbi in zip(fa,fb)]
    ab = fft(fafb,sz,inv=True)
    return [round(x.real) for x in ab[:len(a)+len(b)-1]]

N,M = II()
A = III()

h = [0]*(max(A))
for a in A:
    h[a-1] += 1

conv = [0,0] + convolution(h,h)

ans = 0
for k in range(2,2*max(A)+1)[::-1]:
    if conv[k]<M:
        ans += k*conv[k]
        M -= conv[k]
    else:
        ans += k*M
        break
        
print(ans)