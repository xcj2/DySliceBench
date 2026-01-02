import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    def find_chi(l, r):
        if l == r:
            return l
        min_pre_i = n + 1
        pui = -1
        for ino_i in range(l, r + 1):
            if pre_i[ino_i] < min_pre_i:
                min_pre_i = pre_i[ino_i]
                pui = ino_i
        if pui - l > 0:
            chi[ino[pui]][0] = ino[find_chi(l, pui - 1)]
        if r - pui > 0:
            chi[ino[pui]][1] = ino[find_chi(pui + 1, r)]
        return pui

    def dfs(u):
        l, r = chi[u]
        if l != -1: dfs(l)
        if r != -1: dfs(r)
        pos.append(u)

    n = int(input())
    pre = list(map(int, input().split()))
    ino = list(map(int, input().split()))
    chi = {}
    for u in pre:
        chi[u] = [-1, -1]
    utoi = {u: i for i, u in enumerate(pre)}
    pre_i = []
    for u in ino:
        pre_i.append(utoi[u])
    root = ino[find_chi(0, n - 1)]
    pos = []
    dfs(root)
    print(*pos)

main()

