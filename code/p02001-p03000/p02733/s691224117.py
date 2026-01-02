def inpl():
    return list(map(int, input().split()))


def solve(i):
    def getChoco(choco, w):
        for i in range(H):
            if S[i][w] == "1":
                choco[t[i]] += 1
        return choco

    t = {}
    t[0] = 0
    x = 0
    for h in range(H - 1):
        if (i >> h) % 2 == 1:
            x += 1
            t[h + 1] = x
        else:
            t[h + 1] = x
    choco = [0 for _ in range(x + 1)]
    ret = x
    # print(i, t)

    for w in range(W):
        choco = getChoco(choco, w)
        if any(c > K for c in choco):
            choco = getChoco([0 for _ in range(x + 1)], w)
            if any(c > K for c in choco):
                return H + W - 2
            else:
                ret += 1
    return ret


H, W, K = inpl()
S = [input() for _ in range(H)]

ans = H + W - 2
for i in range(2**(H - 1)):
    ans = min(ans, solve(i))

print(ans)
