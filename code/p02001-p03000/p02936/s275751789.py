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
    n, q = MI()
    e = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = MI1()
        e[a].append(b)
        e[b].append(a)

    point = [0] * n
    for _ in range(q):
        p, x = MI()
        p -= 1
        point[p] += x

    d = deque([(0, point[0])])
    used = [False] * n
    used[0] = True

    while len(d) > 0:
        v, p = d.popleft()
        for nv in e[v]:
            if used[nv]: continue
            used[nv] = True
            point[nv] += p
            d.append((nv, point[nv]))

    printlist(point, " ")

if __name__ == '__main__':
    solve()
