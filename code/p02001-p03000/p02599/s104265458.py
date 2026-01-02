#関数リスト
import sys
from collections import defaultdict
input = sys.stdin.readline
def RD(): return input().rstrip()
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float,input().split()))

class BIT():
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n+1)

    #bit_indexにxをO(log(n))で加算する
    def add(self,i,x):
        #if(i<=0 or i>n):return iに0以下の数字は代入しない
        while i <= self.n:
            self.bit[i] += x
            i += (i & -i)
    #bit_1 + bit_2 + …  + bit_n をO(log(n))で求める
    def sum(self,i):
        s = 0
        #iに0以下の数字は代入しない。
        while i > 0:
            s+=self.bit[i]
            i -= (i & -i)
        return s
    def rangesum(self,i,k):
        return self.sum(k) - self.sum(i)
    #a_1 + a_2 + … + a_i >= x となるような最小のiを求める(a_k >= 0)
    #xが0以下の場合は該当するものなし→0を返す
    def lower_bound(self,x):
        if x <= 0:
            return 0
        else:
            i = 0
            r = 1
            #最大としてありうる区間の長さを取得する
            #n以下の最小の二乗のべき(BITで管理する数列の区間で最大のもの)を求める
            while(r<self.n):
                r=r<<1
            len = r
            while len > 0:
                if(i+len<self.n and self.bit[i+len]<x):
                    x-=self.bit[i+len]
                    i+=len
                len = len >> 1
            return i+1

def main():
    N, Q = MI()
    mylist = LI()
    q = []
    for i in range(Q):
        l, r = MI()
        #データ圧縮
        q.append(r * 10**12 + l * 10**6 + i)
    q.sort()
    last = defaultdict(int)
    r0 = q[0] // 10**12
    for i, c in enumerate(mylist):
        if i+1 > r0:break
        last[c] = i+1
    tree = BIT(N)
    for i in range(N):
        if last[i+1] != 0:
            tree.add(last[i+1], 1)
    ans = [0] * Q
    pre_R = r0
    for x in q:
        r, x = x // 10**12, x % 10**12
        l, q2 = x // 10**6, x % 10**6
        if r > pre_R:
            for i in range(pre_R, r):
                if last[mylist[i]] != 0:
                    tree.add(last[mylist[i]],-1)
                last[mylist[i]] = i+1
                tree.add(i+1,1)
        #ans[q2] = tree.sum(r)-tree.sum(l-1)
        ans[q2] = tree.rangesum(l-1,r)
        pre_R = r
    for a in ans: print(a)

if __name__ == "__main__":
    main()
