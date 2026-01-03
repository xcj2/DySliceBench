def bellmanford(num, start, goal, edges):
    cost = [float('inf')] * num
    cost[start] = 0
    for _ in range(num):
        updated = False
        for a, b, c in edges:
            if cost[b] > cost[a] + c:
                cost[b] = cost[a] + c
                updated = True
        if not updated:
            break
    else:
        return (-1,cost)
    return (1,cost[goal])

def main():
    N, M = LI()
    v = []
    for _ in range(M):
        x, y, z = map(int, input().split())
        v.append((x - 1, y - 1, -z))
#    print(v)
#    print(bellmanford(N, 0, N-1, v))
    cur, d = bellmanford(N, 0, N - 1, v)
    if cur == -1:
        # Nまでの道の途中に負閉路があるか
        inf_flag = [False] * N
        for _ in range(N):
            for f, t, c in v:
                if d[f] == inf: continue
                if inf_flag[f] == True:
                    inf_flag[t] = True
                # 更新が終わっていない→負閉路
                if d[t] > d[f] + c:
                    d[t] = d[f] + c
                    inf_flag[t] = True
        print("inf" if inf_flag[N - 1] else -d[N - 1])
    else:
        print(-d)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LFI(): return list(map(float,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    main()

"""
3 3
1 2 4
2 3 3
1 3 5
"""