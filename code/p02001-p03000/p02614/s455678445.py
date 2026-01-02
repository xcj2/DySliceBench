from itertools import combinations

def make_01(H, W, C):
    ban = [[0 for j in range(W)] for i in range(H)]
    for h in range(H):
        S = C[h]
        for w in range(W):
            if S[w] == '.':
                ban[h][w] = 0
            else:
                ban[h][w] = 1
    return ban

def countban(H, W, hc, wc, ban):
    # print(hc, wc)
    # print(ban)
    for h in hc:
        for w in range(W):
            ban[h][w] = 0
    for w in wc:
        for h in range(H):
            ban[h][w] = 0
    # print(ban)
    val = sum(map(sum, ban))
    # print(val)
    # input()
    return val

def ban_copy(H, W, ban):
    bancopy = [[0 for j in range(W)] for i in range(H)]
    for h in range(H):
        for w in range(W):
            bancopy[h][w] = ban[h][w]
    return bancopy

def main():
    H, W, K = map(int, input().split())
    C = [input() for i in range(H)]
    ban = make_01(H, W, C)
    # print(ban)
    cnt = 0
    for n in range(H + 1):
        for hc in combinations(range(H), n):
            for m in range(W + 1):
                for wc in combinations(range(W), m):
                    tmpc = ban_copy(H, W, ban)
                    if K == countban(H, W, hc, wc, tmpc):
                        cnt += 1
    return cnt

if __name__ == '__main__':
    print(main())
    
    
