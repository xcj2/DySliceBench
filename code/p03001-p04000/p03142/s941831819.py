import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


# トポロジカルソート
# deg[i] := 頂点iの入次数
# returns := トポロジカルソートされた頂点番号のリスト
def tsort(deg, nl):
    tsorted = list()
    stack = [i for i, x in enumerate(deg) if x == 0]
    while len(stack) > 0:
        v = stack.pop()
        tsorted.append(v)
        for next_v in nl[v]:
            deg[next_v] -= 1
            if deg[next_v] == 0:
                stack.append(next_v)
    return tsorted


N, M = MI()

nl = [list() for _ in range(N)]
deg = [0 for _ in range(N)]
for _ in range(N - 1 + M):
    A, B = MI()
    A, B = A - 1, B - 1
    nl[A].append(B)
    deg[B] += 1

tsorted = tsort(deg, nl)

ans = [0] * N
p = {tsorted[0]: -1}
for v in tsorted:
    ans[v] = p[v]
    for next_v in nl[v]:
        p[next_v] = v
for a in ans:
    print(a + 1)