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

# FFT
# use python3
# a = np.array([a1,a2,a3]), b= np.array([b1,b2,b3])
# c = np.array([a1b1,a1b2+a2b1,a1a3+a2b2+a3b1,a2b3+a3b2,a3b3])
import numpy as np
def FFT(a,b):
    bit = (len(a)+len(b)).bit_length()+1
    L = 2**bit
    fa,fb = np.fft.rfft(a,L), np.fft.rfft(b,L)
    c = np.rint(np.fft.irfft(fa*fb,L)).astype(np.int64)
    return c[:len(a)+len(b)-1]

N,M = II()
A = III()

h = [0]*(max(A))
for a in A:
    h[a-1] += 1

conv = np.append([0,0],FFT(h,h))
ans = 0
count = 0

for k in range(2,2*max(A)+1)[::-1]:
    if conv[k]:
        num = min(M-count,conv[k])
        count += num
        ans += k*num
    if count==M:
        break

print(ans)