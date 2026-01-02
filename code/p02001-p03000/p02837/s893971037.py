#!/usr/bin/env python3
import sys
def read(): return sys.stdin.readline() # 標準入力
def fbit(i, j=-1): return format(i, 'b').zfill(j) # bit 表示
def popcount(x): # ビットカウント
    x=x-((x>>1)&0x5555555555555555)
    x=(x&0x3333333333333333)+((x>>2)&0x3333333333333333)
    x=(x+(x>>4))&0x0f0f0f0f0f0f0f0f;x=x+(x>>8);x=x+(x>>16);x=x+(x>>32)
    return x&0x0000007f


def solv(N:int, A, x, y):
    ans = 0
    for bits in range(1<<N):
        ok = True
        count = 0
        for i in range(N):
            if not (bits & 1<<i): continue
            count+=1
            for j in range(A[i]):
                if (bits >> (int(x[i][j])-1) & 1) ^ int(y[i][j]): ok = False
        if ok: ans = max(ans, count);


    print(ans)
def main():
    N = int(read())
    A = []
    x = []
    y = []
    for i in range(N):
        A.append(int(read()))
        _x=[]
        _y=[]
        for j in range(A[-1]):
            [a,b] = list(read().rsplit())
            _x.append(a)
            _y.append(b)
        x.append(_x)
        y.append(_y)


    solv(N, A, x, y)

if __name__ == '__main__':
    main()
