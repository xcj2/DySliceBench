N, W = map(int, input().split())
weights, values = [], []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

def solve(n, w ,weights, values):
    def rec_solve(cw, cv, max_w, i):
        nonlocal weights, values
        #print(cw, cv, i)
        if i == -1:
            return cv
        
        # take
        if weights[i] + cw <= max_w:
            return max(rec_solve(cw+weights[i], cv + values[i], max_w, i-1),
                        rec_solve(cw, cv, max_w, i-1))

        else:
            # dont take
            return rec_solve(cw, cv, max_w, i-1)

    return rec_solve(0, 0, w, n-1)

def solve_fast(n_items, max_w, weights, values):
    dp =  [[0]*(max_w+1) for _ in range(n_items)]
    dp[0] = [values[0] if i >= weights[0] else 0 for i in range(max_w+1)]

    for r in range(1, n_items):
        cw, cv = weights[r], values[r]
        for c in range(max_w+1):
            if cw > c:
                dp[r][c] = dp[r-1][c]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r-1][c-cw] + cv)

    #for r in dp:
        #print(r)

    return dp[-1][-1]


print(solve_fast(N, W, weights, values))