from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

class Searchable_BIT():
    def __init__(self,N):
        self.N = N
        self.node = [0]*(self.N+1)
        self.cnt = 0

    def add(self,a): # 要素 x を追加
        x = a
        self.cnt += 1
        while x <= self.N:
            self.node[x] += 1
            x += x & -x

    def delete(self,x): # 要素 x を削除
        self.cnt -= 1
        while x <= self.N:
            self.node[x] -= 1
            x += x & -x

    def count(self,x): # x以下の要素数
        tmp = 0
        while x > 0:
            tmp += self.node[x]
            x -= x & -x
        return tmp

    def get_maxval(self):
        return self.get_lower_i(self.cnt)

    def get_lower_i(self,i): # i 番目に小さい要素を取得
        NG = -1
        OK = self.N+1
        while OK-NG > 1:
            mid = (OK+NG)//2
            #print(OK,NG,self.count(mid))
            if self.count(mid) >= i:
                OK = mid
            else:
                NG = mid
        return OK

N = inp()
PP = inpl()
inds = [0]*(N+1)
for i,P in enumerate(PP):
    inds[P] = i+1

BIT = Searchable_BIT(N)
ans = 0
for i in reversed(range(1,N+1)):
    ind = inds[i]
    BIT.add(ind)
    cnt = BIT.count(ind)
    Lind1 = BIT.get_lower_i(cnt-1)
    Lind2 = BIT.get_lower_i(cnt-2)
    Rind1 = BIT.get_lower_i(cnt+1)
    Rind2 = BIT.get_lower_i(cnt+2)
    L1 = ind   - Lind1
    L2 = Lind1 - Lind2
    R1 = Rind1 -   ind
    R2 = Rind2 - Rind1
    #print(i,Lind2,Lind1,ind,Rind1,Rind2)
    if Rind1 != N+1:
        ans += i * L1 * R2
    if Lind1 != 0:
        ans += i * L2 * R1


print(ans)
