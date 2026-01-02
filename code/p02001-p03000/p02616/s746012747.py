import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

def solve():
    N, K = mapint()
    As = list(mapint())
    mod = 10**9+7
    pos = []
    neg = []
    for a in As:
        if a>=0:
            pos.append(a)
        else:
            neg.append(a)

    pos.sort(reverse=True)
    neg.sort()
    lenp = len(pos)
    lenn = len(neg)
    if not pos and K%2==1:
        ans = 1
        for i, n in enumerate(neg[::-1]):
            ans *= n
            ans %= mod
            if i==K-1:
                break
        return ans
    if lenp+lenn==K and (K-lenp)%2==1:
        ans = 1
        pos.extend(neg)
        pos.sort(reverse=True)
        for i, p in enumerate(pos):
            ans *= p
            ans %= mod
            if i==K-1:
                break
        return ans
    ans = 1
    pcnt = 0
    ncnt = 0
    for i in range(K//2):
        if pcnt*2+1>=lenp:
            ans *= neg[ncnt*2]*neg[ncnt*2+1]
            ans %= mod
            ncnt += 1
        elif ncnt*2+1>=lenn:
            ans *= pos[pcnt*2]*pos[pcnt*2+1]
            ans %= mod
            pcnt += 1
        elif pos[pcnt*2]*pos[pcnt*2+1]>neg[ncnt*2]*neg[ncnt*2+1]:
            ans *= pos[pcnt*2]*pos[pcnt*2+1]
            ans %= mod
            pcnt += 1
        else:
            ans *= neg[ncnt*2]*neg[ncnt*2+1]
            ans %= mod
            ncnt += 1
    if K%2==1:
        ans *= pos[pcnt*2]
        ans %= mod
    return ans

print(solve())