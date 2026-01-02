import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N, MOD = map(int, input().split())
adjL = [[] for _ in range(N)]
for _ in range(N-1):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    adjL[x].append(y)
    adjL[y].append(x)

def ReRooting(adjL):
    def merge(val1, val2):
        return val1 * val2 % MOD
    def calcValue(val1):
        return (val1 + 1) % MOD

    numV = len(adjL)
    vRoot = 0
    useds = [False] * numV
    useds[vRoot] = True
    vs = [vRoot]
    pars = [-1] * numV
    stack = [vRoot]
    while stack:
        v = stack.pop()
        for v2 in adjL[v]:
            if not useds[v2]:
                useds[v2] = True
                vs.append(v2)
                pars[v2] = v
                stack.append(v2)

    anss = [0] * numV
    dpUpFrom, dpDownTo, accLs, accRs = [1]*numV, [1]*numV, [1]*numV, [1]*numV
    for v in reversed(vs):
        vPar = pars[v]
        tmp = 1
        for v2 in adjL[v]:
            if v2 == vPar: continue
            accLs[v2] = tmp
            tmp = merge(tmp, dpUpFrom[v2])
        tmp = 1
        for v2 in reversed(adjL[v]):
            if v2 == vPar: continue
            accRs[v2] = tmp
            tmp = merge(tmp, dpUpFrom[v2])
        anss[v] = tmp
        dpUpFrom[v] = calcValue(tmp)

    for v in vs:
        vPar = pars[v]
        dpDownToV = dpDownTo[v]
        anss[v] = merge(anss[v], dpDownToV)
        for v2 in adjL[v]:
            if v2 == vPar: continue
            tmp = merge(accLs[v2], accRs[v2])
            tmp = merge(tmp, dpDownToV)
            dpDownTo[v2] = calcValue(tmp)
    return anss

anss = ReRooting(adjL)
print('\n'.join(map(str, anss)))
