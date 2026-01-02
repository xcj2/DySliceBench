import sys
from itertools import combinations

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

    def add(self, i, x):
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
    def ng():
        px=-1
        for i in range(n):
            if i % 2:
                x = xx1[i // 2][1]
            else:
                x = xx0[i // 2][0]
            if x<px:return True
            px=x
        return False

    def change(ans):
        res=0
        bit=BitSum(n)
        for i,k in enumerate(kk):
            res+=i-bit.sum(k)
            if res>ans:return ans
            bit.add(k,1)
        return res

    n = II()
    aa = LI()
    bb = LI()
    ab = []
    for i, (a, b) in enumerate(zip(aa, bb)):
        if i % 2:
            ab.append([b, a, i])
        else:
            ab.append([a, b, i])
    ans=1000
    for odd in combinations(range(n), n // 2):
        isodd = [False] * n
        xx0 = []
        xx1 = []
        for i in odd:
            xx1.append(ab[i])
            isodd[i] = True
        for i in range(n):
            if isodd[i]: continue
            xx0.append(ab[i])
        xx0.sort(key=lambda x: (x[0],x[2]))
        xx1.sort(key=lambda x: (x[1],x[2]))
        #print(xx0)
        #print(xx1)
        if ng():continue
        kk=[]
        for [_,_,i0],[_,_,i1] in zip(xx0,xx1):
            kk+=[i0,i1]
        if n%2:kk+=[xx0[-1][2]]
        #print(kk)
        ans=change(ans)
        #print(ans,xx0,xx1)
    if ans==1000:print(-1)
    else:print(ans)

main()
