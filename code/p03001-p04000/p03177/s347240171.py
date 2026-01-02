from operator import mul

def solve():
    MOD = 10**9 + 7

    N, K = map(int, input().split())
    Ass = [tuple(map(int, input().split())) for _ in range(N)]

    def getMatrixProduct(Ass, Bss, MOD):
        BssTr = map(list, zip(*Bss))
        Ax = len(Ass)
        By = len(Bss[0])
        ansss = [[0]*(By) for _ in range(Ax)]
        for y, Bs in enumerate(BssTr):
            for x, As in enumerate(Ass):
                ansss[x][y] = sum(map(mul, As, Bs)) % MOD
        return ansss
    def getMatrixPower(Ass, n, MOD):
        sizeA = len(Ass)
        ansss = [[0]*(sizeA) for _ in range(sizeA)]
        for i in range(sizeA):
            ansss[i][i] = 1
        while n:
            if n & 1:
                ansss = getMatrixProduct(ansss, Ass, MOD)
            Ass = getMatrixProduct(Ass, Ass, MOD)
            n //= 2
        return ansss

    Pss = getMatrixPower(Ass, K, MOD)

    ans = 0
    for Ps in Pss:
        for P in Ps:
            ans += P
            ans %= MOD

    print(ans)


solve()
