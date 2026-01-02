N, M = map(int, input().split())

E = {a: set() for a in range(1, N + 1)}
for i in range(M):
    a, b = map(int, input().split())
    E[a].add(b)
    E[b].add(a)

def degree(a): return len(E[a])
def nodes():   return range(1, N + 1)

def removeOneCycle():
    """適当なcycleを削除"""
    alive = [a for a in nodes() if degree(a) > 0]
    if len(alive) == 0:
        return False
    lasso = {}   # 投げ縄
    a = alive[0] # 適当な開始節点
    p = None
    while a not in lasso:
        lasso[a] = [b for b in E[a] if b != p][0] # 引き返し以外
        p, a = a, lasso[a]
    start = a
    b = None
    while b != start:
        b = lasso[a]
        E[a].remove(b)
        E[b].remove(a)
        a = b
    return True

yes = all(degree(a) % 2 == 0 for a in nodes()) and \
      removeOneCycle() and \
      removeOneCycle() and \
      any(degree(a) > 0 for a in nodes())

print('Yes' if yes else 'No')
