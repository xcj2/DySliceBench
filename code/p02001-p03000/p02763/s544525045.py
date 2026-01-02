#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**6)

# Segment Tree
class SegmentTree:
    def __init__(self, N):
        self.size = 2 ** (N-1).bit_length()# 要素数を超える最小の2べき
        self.dat = [0] * (2*self.size)
    
    def update(self,i,x):# i番目の文字がxになる
        i += self.size
        self.dat[i] = 1 << ord(x)-ord('a')
        while i > 0:# 上まで更新していく
            i >>= 1
            self.dat[i] = self.dat[i*2] | self.dat[i*2+1]

    def fold(self, l, r):
        l += self.size
        r += self.size
        vl = 0
        vr = 0
        while l < r:
            if l & 1:
                vl |= self.dat[l]
                l += 1
            if r & 1:
                r -= 1
                vr |= self.dat[r]
            l >>= 1
            r >>= 1
        # print(bin(vl | vr))
        return bin(vl | vr).count('1')

def main():
    N = int(input())
    S = list(input())
    sg = SegmentTree(N)
    for i in range(N):
        sg.update(i,S[i])
    
    Q = int(input())
    for _ in range(Q):
        Query = input().split()
        if Query[0] == '1':
            sg.update(int(Query[1])-1, Query[2])
        else:
            res = sg.fold(int(Query[1])-1, int(Query[2]))
            print(res)

if __name__ == "__main__":
    main()