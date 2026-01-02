def examA():
    N, X, T = LI()
    ans = (1 + (N-1)//X)*T
    print(ans)
    return

def examB():
    N = SI()
    s = 0
    for n in N:
        s += int(n)
    if s%9==0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
    return

def examC():
    N = I()
    A = LI()
    now = A[0]
    cnt = 0
    for i in range(N):
        if now>A[i]:
            cnt += now-A[i]
        if now<A[i]:
            now = A[i]
    ans = cnt
    print(ans)
    return

def examD():
    def bfs_grid(h, w, s, g, maze):
        distance = [[inf] * w for _ in range(h)]

        def bfsg():
            queue = deque()
            queue.append(s)
            cost = 0
            distance[s[0]][s[1]] = cost
            used = [s]
            while(True):
                while len(queue):
                    y, x = queue.popleft()
                    for i in range(4):
                        nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]
                        if (0 <= nx < w and 0 <= ny < h and maze[ny][nx] != '#'):
                            if distance[ny][nx] != inf:
                                continue
                            queue.append((ny, nx))
                            distance[ny][nx] = cost
                            used.append((ny,nx))

                #print(used)

                if distance[g[0]][g[1]]==inf:
                    cost += 1
                    used_ne = []
                    for y,x in used:
                        for i in range(5):
                            nx = x + [-2, -1, 0, 1, 2][i]
                            if not 0<=nx<W:
                                continue
                            for j in range(5):
                                ny = y + [-2, -1, 0, 1, 2][j]
                                if not 0<=ny<H:
                                    continue
                                if distance[ny][nx] != inf:
                                    continue
                                if maze[ny][nx]=="#":
                                    continue
                                queue.append((ny,nx))
                                distance[ny][nx] = cost
                                used_ne.append((ny,nx))
                    used = used_ne

                    if not queue:
                        #print(distance)
                        return -1
                    continue

                return cost


            return distance

        return bfsg()
    H, W = LI()
    C = LI()
    D = LI()
    C[0] -= 1; C[1] -= 1
    D[0] -= 1; D[1] -= 1
    S = [SI()for _ in range(H)]
    ans = bfs_grid(H, W, C, D, S)
    print(ans)
    return

def examE():
    H, W, M = LI()
    S = set()
    SH = [[0,i]for i in range(W)]
    SW = [[0,i]for i in range(H)]
    for _ in range(M):
        h, w = LI()
        h -= 1; w -= 1
        S.add((h,w))
        SW[h][0] += 1
        SH[w][0] += 1
    #print(S)
    SH.sort(reverse=True)
    SW.sort(reverse=True)
    #print(SH)
    #print(SW)
    max_SH = SH[0][0]
    max_SW = SW[0][0]
    for h in range(H):
        if SW[h][0]!=max_SW:
            break
        h1 = SW[h][1]
        for w in range(W):
            if SH[w][0] != max_SH:
                break
            w1 = SH[w][1]
            if (h1,w1) not in S:
                #print(h1,w1)
                ans = max_SH+max_SW
                print(ans)
                return

    ans = max_SH+max_SW-1
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import getcontext,Decimal as dec
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
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""