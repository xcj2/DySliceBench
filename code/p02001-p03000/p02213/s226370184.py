import sys
sys.setrecursionlimit(pow(10, 8))

S = [6, 3, 1, 4, 2, 5]
H, W = map(int, input().split())
X = []
for i in range(H):
    X.append(input().strip())

def migi(S):
    return [S[1], S[2], S[3], S[0], S[4], S[5]]
def hidari(S):
    return [S[3], S[0], S[1], S[2], S[4], S[5]]
def sita(S):
    return [S[4], S[1], S[5], S[3], S[2], S[0]]
def ue(S):
    return [S[5], S[1], S[4], S[3], S[0], S[2]]

vs = set()

def dfs(x, y, s):
    if (x, y) == (H-1, W-1):
        return True
    vs.add((x, y))
    f = False
    if x+1 < H and (x+1, y) not in vs:
        ns = sita(s)
        if str(ns[0]) == X[x+1][y]:
            f = f|dfs(x+1, y, ns)
    if y+1 < W and (x, y+1) not in vs:
        ns = migi(s)
        if str(ns[0]) == X[x][y+1]:
            f = f|dfs(x, y+1, ns)
    if x-1 >= 0 and (x-1, y) not in vs:
        ns = ue(s)
        if str(ns[0]) == X[x-1][y]:
            f = f|dfs(x-1, y, ns)
    if y-1 >= 0 and (x, y-1) not in vs:
        ns = hidari(s)
        if str(ns[0]) == X[x][y-1]:
            f = f|dfs(x, y-1, ns)
    return f
if dfs(0, 0, S):
    print("YES")
else:
    print("NO")

