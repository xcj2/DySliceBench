
def matmul(mt1, mt2, n, modp):
    ans = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += mt1[i][k] * mt2[k][j]
                ans[i][j] %= modp
    return ans


def pow_matrix(mt, k, n, modp):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ans[i][i] = 1

    while k:
        if k % 2:
            ans = matmul(ans, mt, n, modp)
        mt = matmul(mt, mt, n, modp)
        k //= 2
    return ans


def submit():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    modp = 10 ** 9 + 7
    ak = pow_matrix(a, k, n, modp)
    
    ans = 0
    for ar in ak:
        for ac in ar:
            ans += ac
            ans %= modp
    print(ans)

submit()
