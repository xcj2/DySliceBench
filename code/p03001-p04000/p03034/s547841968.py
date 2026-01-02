def examA():
    A, P = LI()
    ans = (A*3+P)//2
    print(ans)
    return

def examB():
    N = I()
    SP = [[]for _ in range(N)]
    for i in range(N):
        SP[i] = LSI()
        SP[i][1] = int(SP[i][1])
        SP[i].append(i)
#    print(SP)
    SP = sorted(SP,key = lambda x:x[1], reverse = True)
    SP = sorted(SP,key = lambda x:x[0])
#    print(SP)
    for v in SP:
        print(v[2]+1)
    return

def examC():
    N, M = LI()
    S = [LI() for _ in range(M)]
    P = LI()
    ans = 0
    loop = 2**N
    for i in range(loop):
        flag = True
        d = defaultdict(bool)
        for j in range(N):
            if i&(1<<j)==(1<<j):
                d[j+1] = True
        for l,j in enumerate(S):
            cur = 0
            for k in range(1,j[0]+1):
                if d[j[k]]:
                    cur +=1
            if cur%2!=P[l]:
#                print(cur,l,i)
                flag = False
                break
        if flag:
            ans +=1
    print(ans)

    return

def examE():
    # 区間加算、上書き、一点取得
    class SegmentTree:
        def __init__(self, n, ele, segfun):
            #####単位元######要設定0or1orinf
            self.ide_ele = ele
            self.segfun = segfun
            ####################
            self.n = n
            self.N0 = 1 << n.bit_length()
            self.data = [self.ide_ele] * (self.N0 * 2)

        def update_add(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] += val
                    l += 1
                if r & 1:
                    self.data[r - 1] += val
                    r -= 1
                l //= 2
                r //= 2

        def update(self, l, r, val):
            l += self.N0
            r += self.N0
            while l < r:
                if l & 1:
                    self.data[l] = self.segfun(self.data[l], val)
                    l += 1
                if r & 1:
                    self.data[r - 1] = self.segfun(self.data[r - 1], val)
                    r -= 1
                l //= 2
                r //= 2

        def query(self, i):
            i += len(self.data) // 2
            ret = self.data[i]
            while i > 0:
                i //= 2
                ret = self.segfun(ret, self.data[i])
            return ret
    N, Q = LI()
    X = [LI() for _ in range(N)]
    D = [I() for _ in range(Q)]
    S = SegmentTree(Q+N,inf,lambda a, b: min(a,b))
    QD = []
    for s,t,x in X:
        QD.append([max(0,s-x),t-x,x,0])
    for d in D:
        QD.append([d,1])
    QD.sort(key = lambda x:x[0])
    print(QD)
    ans = []
    for l in QD:
        if l[-1]==0:
            S.update(l[0],l[1],l[2])
        else:
            ans.append(S.query(l[0]))
    for v in ans:
        if v==inf:
            print(-1)
            continue
        print(v)
    return

# 解説AC
def examF():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    def judge(a,c,k):
        if gcd(a,c)==c:
            if c*k>=a:
                return False
        return True
    N = I()
    S = LI()
    ans = -inf
    N -= 1
    F = [defaultdict(int)for _ in range(N)]
    for c in range(1,N):
        K = (N-1)//c
        for k in range(K):
            F[c][k+1] = F[c][k] + S[N-k*c] + S[k*c]
            #print(S[N-k*c], S[k*c])
            a = N - (k+1)*c + c
            cur = F[c][k+1]
            if judge(a,c,k):
                if ans<cur:
                    ans = cur
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examF()
