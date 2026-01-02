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

    out = []
    for i in range(N-1):
        a, b = MI1()
        E[a].append(b)
        E[b].append(a)
        out.append((a, b))

    q = deque([(0, -1, -1)])
    memo = {}
    max_color = 0
    while len(q) > 0:
        current, v_pre, c_pre = q.popleft()
        color = 1
        for nv in E[current]:
            if nv == v_pre: continue
            if color == c_pre:
                color += 1
            q.append((nv, current, color))
            memo[(min(nv, current), max(nv, current))] = color
            max_color = max(max_color, color)
            color += 1
    # print(memo)

    print(max_color)
    for t in out:
        print(memo[t])

if __name__ == '__main__':
    solve()
