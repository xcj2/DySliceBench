# 愚直にやったけど、もうちょいよい方法はないものか
def genP(W):
    P = []
    D = [0]*(W-1)
    P.append(D[:])
    for i in range(2**(W-1)-1):
        d = 0
        while D[d] == 1:
            D[d] = 0
            d+=1
        D[d] = 1
        if any(D[i] == 1 and D[i+1] == 1 for i in range(W-2)):
            continue
        P.append(D[:])
    return P 

# ここがちょっと煩雑
def make_swap(p, W):
    base = [x for x in range(0,W)]
    b = base[:] 
    for w in range(len(p)):
        if p[w] == 1:
            b[w], b[w+1] = b[w+1], b[w]
    return b


def solve(H, W, K):
    swaps = []
    for p in genP(W):
        s = make_swap(p, W)
        swaps.append(s)

    count = [[0]*W for i in range(H+1)]
    count[0][0] = 1

    for h in range(0,H):
        for w in range(0, W):
            for swap in swaps:
                count[h+1][w] += count[h][swap[w]]
                count[h+1][w] %= 1000000007
    #print(count[H])
    print(count[H][K-1])

def main():
    H, W, K = map(int, input().split())
    solve(H, W, K)
main()
