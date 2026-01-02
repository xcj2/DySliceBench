def examA():
    def bfs_grid(h, w, s, maze):
        distance = [[inf] * w for _ in range(h)]

        def bfsg():
            queue = deque()
            if maze[s[0]][s[1]]=="#":
                queue.append((s, 1))
                distance[s[0]][s[1]] = 1
            else:
                queue.append((s,0))
                distance[s[0]][s[1]] = 0
            while len(queue):
                [y, x],st = queue.popleft()
                for i in range(2):
                    nx, ny = x + [1, 0][i], y + [0, 1][i]
                    if (0 <= nx < w and 0 <= ny < h):
                        cur = deepcopy(distance[y][x])
                        if st==0 and maze[ny][nx]=='#':
                            cur += 1
                        if distance[ny][nx] <= cur:
                            continue
                        if maze[ny][nx]=='#':
                            queue.append(((ny, nx),1))
                        else:
                            queue.append(((ny, nx), 0))
                        distance[ny][nx] = cur
            return distance

        return bfsg()
    H, W = LI()
    S = [SI()for _ in range(H)]
    L = bfs_grid(H,W,[0,0],S)
    ans = L[-1][-1]
    #print(L)
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
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
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
    examA()

"""

"""