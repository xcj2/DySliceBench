def examA():
    class Dijkstra(object):
        """
        construct: O(ElogV)
        """
        def __init__(self, edges, start=0):
            """
            :param list of list of list of int edges:
            :param int start=0:
            """
            self.__dist = [inf] * len(edges)
            self.__dist[start] = 0
            self.__calculate(edges, start)

        @property
        def dist(self):
            return self.__dist

        def __calculate(self, edges, start):
            Q = [(0, start)]  # (dist,vertex)
            while (Q):
                dist, v = heapq.heappop(Q)
                if self.dist[v] < dist: continue  # 候補として挙がったd,vだが、他に短いのがある
                for u, cost in edges[v]:
                    if self.dist[u] > self.dist[v] + cost:
                        self.__dist[u] = self.dist[v] + cost
                        heapq.heappush(Q, (self.dist[u], u))
    N, L = LI()
    V, D = LI()
    X = [LI()for _ in range(N)]
    X.append([0,V,D])
    X.append([L,0,0])
    X.sort()
    V = [[]for _ in range(N+2)]
    for i in range(N+1):
        x1, v1, d1 = X[i]
        r = x1 + d1
        for j in range(i+1,N+2):
            x2, v2, d2 = X[j]
            if r<x2:
                break
            cost = (x2-x1)/v1
            V[i].append((j,cost))

    dij = Dijkstra(V, 0)
    ans = dij.dist[-1]
    if ans>=inf:
        print("impossible")
        return
    print('{:.18f}'.format(ans))
    return

def examB():
    N, K = LI()
    H = 11; W = 7
    S = [[0]*(W+1) for _ in range(H+3)]
    for h in range(H+2):
        for w in range(W):
            S[h+1][w+1] = (S[h][w+1] + S[h+1][w] - S[h][w] + (7*h+w+1))
    #print(S)
    base = 0
    for h in range(H):
        for w in range(W-2):
            cur = S[h+3][w+3] - S[h+3][w] - S[h][w+3] + S[h][w]
            if cur%11==K:
                base += 1
                #print(h,w)
    ans = base * ((N-2)//11)
    #print(ans)
    rest = (N-2)%11
    for h in range(rest):
        for w in range(W-2):
            cur = S[h+3][w+3] - S[h+3][w] - S[h][w+3] + S[h][w]
            if cur%11==K:
                ans += 1
                #print(h,w)
    print(ans)
    return

def examC():
    N, K = LI()
    A = LI()
    loop = 2**N
    ans = inf
    for i in range(loop):
        cnt = 0
        need = 0
        highest = 0
        for j in range(N):
            if i&(1<<j)==0:
                if highest<A[j]:
                    need = inf
                    break
                continue
            cnt += 1
            if highest>=A[j]:
                need += (highest+1-A[j])
                highest = highest + 1
            else:
                highest = A[j]
        if cnt>=K and need<ans:
            ans = need
        #print(need)
    print(ans)
    return

def examD():
    # 参考 https://qiita.com/maskot1977/items/e1819b7a1053eb9f7d61
    def cycle(neighbor, start, ring_size, node):
        visited = [False]*node
        stack = []
        stack.append([start])
        visited[start] = True
        while (stack):
            curr_path = stack.pop()
            #check = deepcopy(curr_path)
            #check = set(check)
            if len(curr_path) > ring_size:
                continue
            # print curr_path
            last = curr_path[-1]
            for nei in neighbor[last]:
                if nei in curr_path:
                    if len(curr_path)==0:
                        continue
                    if (len(curr_path) <= ring_size) and (curr_path[0] == nei):
                        new_path = copy(curr_path)
                        return new_path
                    elif (len(curr_path) <= ring_size):
                        return cycle(neighbor,nei,ring_size-1,node)
                if visited[nei]:
                    continue
                visited[nei] = True
                new_path = copy(curr_path)
                new_path.append(nei)
                stack.append(new_path)
        return -1
    N, M = LI()
    V = [[]for _ in range(N)]
    for _ in range(M):
        a,b = LI()
        a -= 1; b -= 1
        V[a].append(b)
    #print(V)
    loop = -1
    for i in range(N):
        loop = cycle(V,i,N,N)
        if loop!=-1:
            break
    if loop==-1:
        print(-1)
        return
    while(True):
        next = -1
        for k in loop:
            next = cycle(V,k,len(loop)-1,N)
            if next != -1:
                break
        if next==-1:
            break
        loop = next

    ans = loop
    print(len(ans))
    for v in ans:
        print(v+1)
    return

import sys,bisect,itertools,heapq,math,random
from copy import copy,deepcopy
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
    examD()
