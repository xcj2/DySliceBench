def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    H, W = read_values()
    S = [input() for _ in range(H)]
    X = [[0 for _ in range(W)] for __ in range(H)]
    Y = [[0 for _ in range(W)] for __ in range(H)]

    for h in range(H):
        for w in range(W):
            if S[h][w] == ".":
                X[h][w] = 1 if w == 0 else X[h][w - 1] + 1
                Y[h][w] = 1 if h == 0 else Y[h - 1][w] + 1

    res = 0
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if S[h][w] == "#":
                continue
            if w != W - 1:
                X[h][w] = max(X[h][w + 1], X[h][w]) 
            if h != H - 1:
                Y[h][w] = max(Y[h + 1][w], Y[h][w])
            res = max(res, X[h][w] + Y[h][w] - 1)
    print(res)

        
if __name__ == "__main__":
    main()

