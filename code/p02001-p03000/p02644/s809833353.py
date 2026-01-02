def examA():
    X = LI()
    for i in range(len(X)):
        if X[i]==0:
            ans = i+1
    print(ans)
    return

def examB():
    X, Y = LI()
    ans = "No"
    for i in range(X+1):
        if i*2+(X-i)*4==Y:
            ans = "Yes"
    print(ans)
    return

def examC():
    X, N = LI()
    P = LI()
    P = set(P)
    cur = inf
    ans = -1
    for i in range(-1,102):
        if i in P:
            continue
        now = abs(i-X)
        if now<cur:
            ans = i
            cur = now
    print(ans)
    return

def examD():
    def make_divisors(n):
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        # divisors.sort()
        return divisors
    N = I()
    A = LI()
    C = set()
    n = 10**6+1
    D = [False]*n
    ans = 0
    for a in A:
        if a in D:
            D[a] = False
            continue
        D[a] = True
        C.add(a)

    for a in C:
        for i in range(2,1+n//a):
            D[i*a] = False
    ans = sum(D)
    print(ans)
    return

def examE():
    N, Q = LI()
    AB = [LI()for _ in range(N)]



    ans = 0
    print(ans)
    return

def examF():
    H, W, K = LI()
    x1,y1,x2,y2 = LI()
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    C = [SI()for _ in range(H)]

    def bfs_grid(h, w, s, maze):
        distance = [[inf] * w for _ in range(h)]

        def bfsg():
            queue_up = deque()
            queue_d = deque()
            queue_r = deque()
            queue_l = deque()
            queue_up.append(s)
            queue_d.append(s)
            queue_r.append(s)
            queue_l.append(s)
            distance[s[0]][s[1]] = 0
            while (len(queue_up) or len(queue_r) or len(queue_d) or len(queue_l)):
                if queue_up:
                    y, x = queue_up.popleft()
                    for k in range(1, K + 1):
                        nx, ny = x, y + k
                        if (0 <= nx < w and 0 <= ny < h and maze[ny][nx] != '@'):
                            if distance[ny][nx] <= distance[y][x] + 1:
                                continue
                            queue_r.append((ny, nx))
                            queue_l.append((ny, nx))
                            distance[ny][nx] = distance[y][x] + 1
                        else:
                            break
                        if k == K:
                            queue_up.append((ny, nx))
                if queue_d:
                    y, x = queue_d.popleft()
                    for k in range(1, K + 1):
                        nx, ny = x, y - k
                        if (0 <= nx < w and 0 <= ny < h and maze[ny][nx] != '@'):
                            if distance[ny][nx] <= distance[y][x] + 1:
                                continue
                            queue_r.append((ny, nx))
                            queue_l.append((ny, nx))
                            distance[ny][nx] = distance[y][x] + 1
                        else:
                            break
                        if k == K:
                            queue_d.append((ny, nx))
                if queue_r:
                    y, x = queue_r.popleft()
                    for k in range(1, K + 1):
                        nx, ny = x + k, y
                        if (0 <= nx < w and 0 <= ny < h and maze[ny][nx] != '@'):
                            if distance[ny][nx] <= distance[y][x] + 1:
                                continue
                            queue_up.append((ny, nx))
                            queue_d.append((ny, nx))
                            distance[ny][nx] = distance[y][x] + 1
                        else:
                            break
                        if k == K:
                            queue_r.append((ny, nx))
                if queue_l:
                    y, x = queue_l.popleft()
                    for k in range(1, K + 1):
                        nx, ny = x - k, y
                        if (0 <= nx < w and 0 <= ny < h and maze[ny][nx] != '@'):
                            if distance[ny][nx] <= distance[y][x] + 1:
                                continue
                            queue_up.append((ny, nx))
                            queue_d.append((ny, nx))
                            distance[ny][nx] = distance[y][x] + 1
                        else:
                            break
                        if k == K:
                            queue_l.append((ny, nx))

            return distance

        return bfsg()
    L = bfs_grid(H,W,(x1,y1),C)
    #print(L)
    ans = L[x2][y2]
    if ans==inf:
        ans = -1
    print(ans)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""