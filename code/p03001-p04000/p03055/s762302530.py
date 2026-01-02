def examA():
    N = I()
    ans = 0
    print(ans)
    return

# maspyさん
def examB_maspy():
    H, W, N = LI()
    sr, sc = LI()
    S = SI()
    T = SI()
    sr = H + 1 - sr

    # ここに居たら後手の価値
    L, R = 1, W
    D, U = 1, H
    for s, t in zip(S[::-1], T[::-1]):
        if t == 'L':
            R += 1
        elif t == 'D':
            U += 1
        elif t == 'R':
            L -= 1
        elif t == 'U':
            D -= 1

        if L == 0: L = 1
        if D == 0: D = 1
        if R > W: R = W
        if U > H: U = H

        if s == 'L':
            L += 1
        elif s == 'R':
            R -= 1
        elif s == 'D':
            D += 1
        elif s == 'U':
            U -= 1

        if L > R or D > U:
            # 後手の勝てる場所が存在せず
            break

    bl = (L <= sc <= R) and (D <= sr <= U)
    answer = 'YES' if bl else 'NO'
    print(answer)
    return

#自分の H+1-Start[0]忘れ
def examB():
    H, W, N = LI()
    start = LI()
    S = SI();
    T = SI()
    for t, a in [["U", "D"], ["R", "L"]]:
        if t == "U":
            n = H
        else:
            n = W
        # 落ちないエリア
        l = 1;
        r = n
        if S[-1] == t:
            r -= 1
        elif S[-1] == a:
            l += 1
        for i in range(N - 2, -1, -1):
            if T[i] == t and l > 1:
                l -= 1
            elif T[i] == a and r < n:
                r += 1
            if S[i] == t:
                r -= 1
            elif S[i] == a:
                l += 1
            #            print(l,r)
            if l > r:
                print("NO")
                return
            if t == "U" and (r == 0 or l == n):
                print("NO")
                return
            if t == "R" and (r == 0 or l == n):
                print("NO")
                return

        if t == "U" and (not l <= H + 1 - start[0] <= r):
            print("NO")
            return
        elif t == "R" and (not l <= start[1] <= r):
            print("NO")
            return
    print("YES")
    return

def examC():
    def bfs(n, e, fordfs):
        # 点の数、スタートの点、有向グラフ
        W = [-1] * n
        # 各点の状態量、最短距離とか,見たかどうかとか
        W[e] = 0
        que = deque()
        que.append(e)
        while que:
            now = que.popleft()
            nowW = W[now]
            for ne in fordfs[now]:
                if W[ne] == -1:
                    W[ne] = nowW + 1
                    que.append(ne)
        return W
    N = I()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -=1; b -=1
        V[a].append(b)
        V[b].append(a)
    L = bfs(N,0,V)
    D = max(bfs(N,L.index(max(L)),V))
#    print(D)
    if D%3==1:
        print("Second")
    else:
        print("First")
    return

def examD():
    ans = 0
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
    examC()

"""

"""