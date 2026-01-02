def wf(c):
    d = {}
    for i in range(10):
        for j in range(10):
            d[(i,j)] = c[i][j]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                if d[(i,j)] > d[(i,k)] + d[(k,j)]:
                    d[(i,j)] = d[(i,k)] + d[(k,j)]
    e = {}
    for i in range(10):
        e[i] = d[(i,1)]
    return e


def solve(H, W, c, A):
    d = wf(c)
    mp = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                mp += d[A[i][j]]
    return mp


def main():
    H, W = list(map(int, input().split(' ')))
    c = []
    for i in range(10):
        c.append(list(map(int, input().split(' '))))
    A = []
    for i in range(H):
        A.append(list(map(int, input().split(' '))))

    ans = solve(H, W, c, A)
    print(ans)



if __name__ == '__main__':
    main()