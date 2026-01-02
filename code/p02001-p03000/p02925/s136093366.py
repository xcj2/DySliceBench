def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
    print(ans)
    return

def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    N = I()
    node = N*(N-1)//2
    V = [[]for _ in range(node)]
    D = [[0]*N for _ in range(N)]
    cur = 0
    for i in range(N):
        for j in range(i+1,N):
            D[i][j] = cur
            D[j][i] = cur
            cur += 1
    #A = [LI() for _ in range(N)]
    for i in range(N):
        a = LI()
        for j in range(N-2):
            fr = D[i][a[j]-1]
            to = D[i][a[j+1]-1]
            #print(fr,to)
            V[fr].append(to)

    visited = [False] * node
    calculated = [False] * node
    dp = [1] * node
    # https://mhiro216.hatenablog.com/entry/2019/09/08/142414
    def dfs(v):
        if visited[v]:
            if not calculated[v]:
                return -1  # 計算が終わっていない頂点を2度訪れるのはループがあるということ
            return dp[v]
        visited[v] = True
        for u in V[v]:  # 全ての辺をなめる
            res = dfs(u)
            if res == -1: return -1  # ループがあれば-1を返す
            elif res+1>dp[v]:
                dp[v] = res + 1
        calculated[v] = True
        return dp[v]

    ans = 0
    for i in range(node):
        res = dfs(i)
        ans = max(ans,res)
        if res == -1:
            print('-1')  # ループがあれば-1を返す（問題文の指示）
            return
    print(ans)
    return

def examE2():
    N = I()
    node = N*(N-1)//2
    V = [[]for _ in range(node)]
    D = [[0]*N for _ in range(N)]
    cur = 0
    for i in range(N):
        for j in range(i+1,N):
            D[i][j] = cur
            D[j][i] = cur
            cur += 1
    #A = [LI() for _ in range(N)]
    for i in range(N):
        a = LI()
        for j in range(N-2):
            fr = D[i][a[j]-1]
            to = D[i][a[j+1]-1]
            #print(fr,to)
            V[fr].append(to)
    #print(V)


    # 閉路検出
    def hasCycle(n,V):
        visited = [False]*n
        used = [False]*n

        def dfs(s, p=-1):
            if used[s]:
                return False

            now_use.add(s)

            for v in V[s]:
                if visited[v]:
                    return True
                if v in now_use:
                    continue
                visited[v] = True
                res = dfs(v, s)
                visited[v] = False
                if res:
                    return True
            return False

        has_cycle = False

        for i in range(node):
            now_use = set()
            if used[i]:
                continue
            visited[i] = True
            if dfs(i):
                has_cycle = True
                break
            for u in now_use:
                used[u] = True
            visited[i] = False

        return has_cycle

    if hasCycle(node,V):
        print(-1)
        return

    def getMaxLength(n,V):
        visited = [False]*n
        max_lens = [0] * n

        def dfs(s,p=-1):
            res = 0

            for v in V[s]:
                if max_lens[v]>0:
                    child = max_lens[v]
                else:
                    visited[v] = True
                    child = dfs(v, s)
                    visited[v] = False
                if res<child:
                    res = child
            max_lens[s] = res + 1

            return res+1

        for i in range(n):
            if max_lens[i]>0:
                continue
            length = dfs(i)

        return max(max_lens)

    ans = getMaxLength(node,V)
    print(ans)
    return

def examF():
    # 合ってんのこれ?????
    def calc_L(a,b):
        return (a**2 + b**2)**(1/2)
    N = I()
    X = [[]for _ in range(N)]
    for i in range(N):
        x,y = LI()
        d = math.degrees(math.atan2(y,x))
        if d<0:
            d += 360
        X[i] = [d,x,y]
    X.sort()
    #print(X)
    ans = 0
    for i in range(N):
        cur_X = 0; cur_Y = 0
        for d2,x2,y2 in (X[i:] + X[:i]):
            if calc_L(cur_X+x2,cur_Y+y2)<calc_L(cur_X,cur_Y):
                continue
            cur_X += x2
            cur_Y += y2

        now = calc_L(cur_X,cur_Y)
        if now>ans:
            ans = now

    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examE2()

"""

"""