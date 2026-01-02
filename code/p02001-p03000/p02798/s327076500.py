def examA():
    H = I()
    W = I()
    N = I()
    ans = (N-1)//max(H,W) + 1
    print(ans)
    return

def examB():
    N = I()
    XL = [LI()for _ in range(N)]
    for i in range(N):
        XL[i][0] += XL[i][1]
    XL.sort()
#    print(XL)
    ans = 0
    now = -inf
    for i in range(N):
        if XL[i][0]-XL[i][1]*2>=now:
            ans +=1
            now = XL[i][0]
    print(ans)
    return

def examC():
    N, K, S = LI()
    A = [0]*N
    if S>=10**6:
        a = 1
    else:
        a = S+1
    for i in range(N):
        if i<K:
            A[i] = S
        else:
            A[i] = a
    print(" ".join(map(str,A)))
    return

def examD():
    N = I()
    A = LI()
    B = LI()
    loop = 2**N
    ans = inf
    for i in range(loop):
        cur = 0
        nowA = []
        l = -1; r = 0
        for j in range(N):
            if i&(1<<j)==(1<<j):
                cur +=1
                nowA.append(B[j])
                if l==-1:
                    l = j
                r = j+1
            else:
                nowA.append(A[j])
        if cur%2==1:
            continue
        if l==-1:
            l = 0
        pr = sorted(nowA)
#        print(nowA,pr)
        now = 0
        for j in range(N):
            dist = [i for i, x in enumerate(pr) if x == nowA[j]]
#            print(dist)
            candi = inf
            for v in dist:
                if ((abs(v-j)%2)==1 and i&(1<<j)==(1<<j)):
                    candi = min(candi,abs(v-j))
                if ((abs(v-j)%2)==0 and i&(1<<j)==0):
                    candi = min(candi,abs(v-j))
            if candi==inf:
#                print(dist, i & (1 << j),i,j)
                now = inf
                break
            else:
                if candi==0 and l<=j<r:
                    candi = 2
                now +=candi
#        if (now//2)%2==(r-l)%2:
        ans = min(ans,now)
#        print(now)
    if ans==inf:
        print(-1)
    else:
        print(ans//2)
    return

def examD2():
    # 0は絶対に入れない!!
    class Bit():
        def __init__(self, n):
            self.size = n
            self.tree = [0] * (n + 1)
            return

        def sum(self, i):
            s = 0
            while i > 0:
                s += self.tree[i]
                i -= i & -i
            return s

        def add(self, i, x=1):
            # i==0 はだめ => 全部+1するとか
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def search(self, x):
            # 二分探索。和がx以上となる最小のインデックス(>= 1)を返す
            # maspyさんの参考　よくわかってない
            i = 0
            s = 0
            step = 1 << ((self.size).bit_length() - 1)
            while step:
                if i + step <= self.size and s + self.tree[i + step] < x:
                    i += step
                    s += self.tree[i]
                step >>= 1
            return i + 1

        def debug(self, k):
            return [self.sum(i) for i in range(k)]

        def inversion(self, A=[3, 10, 1, 8, 5]):
            res = 0
            for i, p in enumerate(A):
                self.add(p, 1)
                res += i + 1 - self.sum(p)
            return res

    N = I()
    A = LI()
    B = LI()
    ans = inf
    loop = 1<<N
    for l in range(loop):
        LO = []
        LE = []
        for j in range(N):
            if l&(1<<j)>0:
                if j%2==0:
                    LE.append((B[j],j+1))
                else:
                    LO.append((B[j],j+1))
            else:
                if j%2==0:
                    LO.append((A[j],j+1))
                else:
                    LE.append((A[j],j+1))
        if (len(LO)-len(LE))!=N%2:
            continue
        LO.sort()
        LE.sort()
        L = []
        L.append(LO[0][1])
        flag = True
        for i in range(1,N):
            if i%2==1:
                if LE[i//2][0]>=LO[i//2][0]:
                    L.append(LE[i//2][1])
                else:
                    flag = False
                    break
            else:
                if LO[i//2][0]>=LE[i//2-1][0]:
                    L.append(LO[i//2][1])
                else:
                    flag = False
                    break

        if flag:
            bit = Bit(N+1)
            now = bit.inversion(L)
            if ans > now:
                ans = now
    if ans==inf:
        ans = -1
    print(ans)
    return

def examD3():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    UP = (N + 1) // 2
    DOWN = N - UP

    ANS = 1 << 31

    def ten(A):
        LEN = len(A)
        MAX = max(A)
        MIN = min(A)

        BIT = [0] * (MAX - MIN + 2)  # 出現回数をbit indexed treeの形でもっておく.

        def update(v, w):  # index vにwを加える
            while v <= MAX - MIN + 1:
                BIT[v] += w
                v += (v & (-v))  # 自分を含む大きなノードへ. たとえばv=3→v=4

        def getvalue(v):  # MIN～vの区間の和を求める
            ANS = 0
            while v != 0:
                ANS += BIT[v]
                v -= (v & (-v))  # たとえばv=3→v=2へ
            return ANS

        ANS = 0
        for i in range(LEN):  # A[0],A[1],...とBITを更新しながら,各A[i]について転倒数を求める.
            bit_ai = A[i] - MIN + 1  # A[i]がBITの中で何番目か

            ANS += i  # 今まで出現した個数.
            ANS -= getvalue(bit_ai)  # 今まで出現した中で,MIN～bit_aiの個数を減らす.
            # bit_ai～MAXの出現個数が転倒数

            update(bit_ai, 1)

        return ANS

    for i in range(1 << N):
        UD = [0, 0]
        S0 = []
        S1 = []

        for j in range(N):
            if (1 << j) & i != 0:
                if j % 2 == 0:
                    S0.append((A[j], j))
                else:
                    S1.append((A[j], j))
                UD[j % 2] += 1

            else:
                if (j + 1) % 2 == 0:
                    S0.append((B[j], j))
                else:
                    S1.append((B[j], j))

                UD[(j + 1) % 2] += 1

        if UD[0] == UP and UD[1] == DOWN:
            S0.sort()
            S1.sort()
            # print(UD,S0,S1)

            for i in range(1, N):
                if i % 2 == 0:
                    if S0[i // 2][0] >= S1[(i - 1) // 2][0]:
                        True
                    else:
                        break
                else:
                    if S1[i // 2][0] >= S0[(i - 1) // 2][0]:
                        True
                    else:
                        break
            else:
                K = []
                for i in range(N):
                    if i % 2 == 0:
                        K.append(S0[i // 2][1])
                    else:
                        K.append(S1[i // 2][1])

                # print(K)
                # print(ten(K))

                ANS = min(ANS, ten(K))

    if ANS == 1 << 31:
        print(-1)
    else:
        print(ANS)
    return

def examE():
    return

from copy import deepcopy
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
    examD2()

"""
4
5 2 3 4
2 8 4 2
"""