import sys
import math
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
    
input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float,input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
    

#乗法のmod逆元
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

# nCr mod m
# modinvが必要
# rがn/2に近いと非常に重くなる
def combination(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res


#べき乗
def Raise(x, y, mod=10**9+7):
    # xをy乗する。
    n = 0
    while True:
        if (1<<n) > y:
            break
        n+=1
    D = [0]*(n+1)
    x = x % mod
    D[0] = x
    index = 0
    for index in range(1,n):
        D[index] = (D[index-1]**2)
    res = 1
    index = 0
    for index in range(0, n):
        if (y>>index)&1 == 1:
            res *= D[index]
    return res


def main():
    #答えは 10^2 - 2*9^2 + 8^2
    n = I()
    res = Raise(10, n)- 2 * Raise(9, n) + Raise(8, n)
    print(res % (10**9+7))
    
if __name__ == "__main__":
    main()