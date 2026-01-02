import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from collections import deque

def solve():
    N = II()
    E = [[] for _ in range(N)]

    for i in range(N-1):
        a, b = MI1()
        E[a].append((b, i))
        E[b].append((a, i))

    q = deque([(0, -1, -1)])
    ans = [0] * (N-1)
    while len(q) > 0:
        current, v_pre, c_pre = q.popleft()
        color = 1
        for (nv, idx) in E[current]:
            if nv == v_pre: continue
            if color == c_pre:
                color += 1
            q.append((nv, current, color))
            ans[idx] = color
            color += 1

    print(max(ans))
    printlist(ans)

if __name__ == '__main__':
    solve()
