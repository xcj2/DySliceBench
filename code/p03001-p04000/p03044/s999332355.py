import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def II(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def SI(): return input()
YN = lambda b: print('YES') if b else print('NO')
yn = lambda b: print('Yes') if b else print('No')


N = II()
u_li = []
v_li = []
w_li = []
for i in range(N-1):
    u, v, w = LI()
    u_li.append(u)
    v_li.append(v)
    w_li.append(w)

# 連結リストを作成。計算量削減のために、距離の情報も持つ。
max_node = max(max(u_li), max(v_li))
neighbor = [[] for i in range(max_node+1)]
for i in range(N-1):
    neighbor[u_li[i]].append((v_li[i], w_li[i]))
    neighbor[v_li[i]].append((u_li[i], w_li[i]))

# 深さ優先探索をしつつ色を塗っていく。
from collections import deque
def depth_first(neighbor, start):
    visited, stack = [False]*(N+1), deque()
    stack.append(start)
    result = [None, 0] + [None]*(N-1)
    while len(stack) > 0:
        next_node = stack.pop()
        if visited[next_node]: continue
        visited[next_node] = True
        for nei in neighbor[next_node]:
            if result[nei[0]] is not None: continue
            if nei[1]%2 == 0:
                result[nei[0]] = result[next_node]
            else:
                result[nei[0]] = (result[next_node]+1)%2
            stack.append(nei[0])
    return result

colors = depth_first(neighbor, 1)

for ans in colors[1:]:
    print(ans)
