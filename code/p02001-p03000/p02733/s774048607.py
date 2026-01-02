def read():
    H, W, K = list(map(int, input().strip().split()))
    S = list()
    for i in range(H):
        s = list(map(int, input()))
        S.append(s)
    return H, W, K, S


def init_n_splits(H, ptn):
    n_splits = 0
    for h in range(1, H):
        if ptn & 1 == 1:
            n_splits += 1
        ptn >>= 1
    return n_splits


def check_first_column(w, H, K, ptn, S):
    k = [0 for h in range(H)]
    k[0] = S[0][w]
    if k[0] > K:
        return [-1 for h in range(H)]
    for h in range(1, H):
        if ptn & 1 == 1:
            k[h] = S[h][w]
        else:
            k[h] = S[h][w] + k[h-1]
        if k[h] > K:
            return [-1 for h in range(H)]
        ptn >>= 1
    return k


def check_next_column(w, H, K, ptn, S, prev):
    k = [0 for h in range(H)]
    k[0] = S[0][w]
    if k[0] + prev[0] > K:
        return [-1 for h in range(H)]
    for h in range(1, H):
        if ptn & 1 == 1:
            k[h] = S[h][w]
        else:
            k[h] = S[h][w] + k[h-1]
        if k[h] + prev[h] > K:
            return [-1 for h in range(H)]
        ptn >>= 1
    return [i + j for i, j in zip(k, prev)]


def solve(H, W, K, S, INF=10000000):
    ptns = 2 ** (H-1)
    min_n_splits = W * H
    for ptn in range(ptns):
        update = True
        n_splits = init_n_splits(H, ptn)
        ret = check_first_column(0, H, K, ptn, S)
        if ret[0] == -1:
            update = False
        else:
            for w in range(1, W):
                prev = ret
                ret = check_next_column(w, H, K, ptn, S, prev)
                if ret[0] == -1:
                    n_splits += 1
                    ret = check_first_column(w, H, K, ptn, S)
                    if ret[0] == -1:
                        update = False
                        break
        if update:
            min_n_splits = min(n_splits, min_n_splits)
    return min_n_splits

if __name__ == '__main__':
    inputs = read()
    print("{}".format(solve(*inputs)))
