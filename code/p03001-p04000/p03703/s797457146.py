import sys
import numpy as np

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

def main():
    n,k=MI()
    aa=np.zeros(n+1,dtype="i8")
    aa[0]=k
    for i in range(1,n+1):
        aa[i]=II()
    aa-=k
    cs=np.cumsum(aa)
    #print(aa)
    #print(cs)
    #座標圧縮
    ss=set()
    for s in cs:
        ss.add(s)
    enc={s:i for i,s in enumerate(sorted(ss))}
    #print(enc)
    #転倒数の要領で、自分より左にある自分以下の数の個数を数える
    bit=BitSum(len(ss))
    ans=0
    for s in cs:
        enc_s=enc[s]
        ans+=bit.sum(enc_s)
        bit.update(enc_s,1)
    print(ans)

main()