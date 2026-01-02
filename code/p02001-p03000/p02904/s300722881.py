import sys
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

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
        OK = self.N
        while OK-NG > 1:
            mid = (OK+NG)//2
            #print(OK,NG,self.count(mid))
            if self.count(mid) >= i:
                OK = mid
            else:
                NG = mid
        return OK

N,K = inpl()
PP = inpl()

BIT = Searchable_BIT(N+1)
for i in range(1,K):
    BIT.add(PP[i]+1)

ans = [i for i in range(N-K+1)]

cnt = 1
for i in range(N-1):
    if PP[i] < PP[i+1]:
        cnt += 1
    else:
        cnt = 1
    if cnt >= K:
        ans[i-K+2] = -1

for i in range(N-K):
    L,R = PP[i]+1,PP[i+K]+1
    MIN,MAX = BIT.get_lower_i(1), BIT.get_maxval()
    if L <= MIN and MAX <= R:
        ans[i+1] = ans[i]
    BIT.delete(PP[i+1]+1)
    BIT.add(PP[i+K]+1)

print(len(set(ans)))
