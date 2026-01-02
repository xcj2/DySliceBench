import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, q = li()
edge = [list(li_()) for _ in range(n-1)]
query = [list(li()) for _ in range(q)]

# 各頂点に指定の数字を入れる
num = [0]*n
for pi, xi in query:
    pi -= 1
    num[pi] += xi

# 木を構築
tree = [[] for _ in range(n)]
for ai, bi in edge:
    tree[ai].append(bi)
    tree[bi].append(ai)


# ルートから、親+自分の数字を入れる
visited = [False]*n
stack = [0]
visited[0] = True

while stack:
    cur = stack.pop()
    for nex in tree[cur]:
        if visited[nex]:
            continue

        visited[nex] = True
        num[nex] += num[cur]
        stack.append(nex)

# 出力
print(*num)
