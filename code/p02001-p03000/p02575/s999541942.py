# -*- coding: utf-8 -*-
import sys 
import heapq
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 

def main():
    
    class BIT:
        def __init__(self,len_A):
            self.N = len_A + 10
            self.bit = [0]*(len_A+10)
        # sum(A0 ~ Ai)
        # O(log N)
        def query(self,i):
            res = 0
            idx = i+1
            while idx:
                res += self.bit[idx]
                idx -= idx&(-idx)
            return res
        # Ai += x
        # O(log N)
        def update(self,i,x):
            idx = i+1
            while idx < self.N:
                self.bit[idx] += x
                idx += idx&(-idx)
        # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
        # O(log N)
        def lower_left(self,w):
            if (w < 0):
                return -1
            x = 0
            k = 1<<(self.N.bit_length()-1)
            while k > 0:
                if x+k < self.N and self.bit[x+k] < w:
                    w -= self.bit[x+k]
                    x += k
                k //= 2
            return x
 
    h,w = map(int,readline().split())
    #dp[i] : iの時の最小右移動回数
    dp = [0]*(w+1)
    #解候補
    res = [0]*w
    #解候補から消されるもの
    anti = []
    C = BIT(w)
    for i in range(1,w+1):
        C.update(i,1)
    for i in range(1,h+1):
        a,b = map(int,readline().split())
        #a-1,b+1の値を計算
        x = a-1
        if x != 0 and x != w+1 and dp[x] == -1:
            #x以下のvalidな個数
            k = C.query(x-1)
            #k番目のvalidな位置okからXに行く
            if k != 0:
                ok = C.lower_left(k)
                #xをvalidにする
                dp[x] = dp[ok] + (x-ok)
                C.update(x,1)
                heapq.heappush(res,dp[x])
                
        x = b+1
        if x != 0 and x != w+1 and dp[x] == -1:
            #x以下のvalidな個数
            k = C.query(x-1)
            #k番目のvalidな位置okからXに行く
            if k != 0:
                ok = C.lower_left(k)
                #xをvalidにする
                dp[x] = dp[ok] + (x-ok)
                C.update(x,1)
                heapq.heappush(res,dp[x])
        k = C.query(a-1)+1
 
        while True:
            ok = C.lower_left(k)
            if ok > b or dp[ok] == -1:
                break
            heapq.heappush(anti,dp[ok])
            dp[ok] = -1
            C.update(ok,-1)
        while anti and res and anti[0] == res[0]:
            heapq.heappop(anti)
            heapq.heappop(res)
        if res:
            print(res[0]+i)
        else:
            print(-1)
if __name__ == '__main__':
    main()