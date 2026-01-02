mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline

    def PrimeDecomposition(N):
        ret = {}
        n = int(N ** 0.5)
        for d in range(2, n + 1):
            while N % d == 0:
                if d not in ret:
                    ret[d] = 1
                else:
                    ret[d] += 1
                N //= d
            if N == 1:
                break
        if N != 1:
            ret[N] = 1
        return ret

    def extgcd(a, b):
        if b:
            d, y, x = extgcd(b, a % b)
            y -= (a // b) * x
            return d, x, y
        else:
            return a, 1, 0

    N = int(input())
    if N == 1:
        print(1)
        exit()
    P = PrimeDecomposition(N)
    if 2 in P:
        P[2] += 1
    else:
        P[2] = 1
    p_list = list(P.keys())
    np = len(p_list)
    ans = 2*N
    for i in range(2 ** np):
        p1 = 1
        p2 = 1
        for j in range(np):
            pp = p_list[j]
            if i >> j & 1:
                p1 *= pp ** P[pp]
            else:
                p2 *= pp ** P[pp]
        _, s2, s1 = extgcd(p2, p1)
        while s1 >= 0 or s2 <= 0:
            s1 -= p2
            s2 += p1
        while s2 - p1 > 0 and s1 + p2 < 0:
            s2 -= p1
            s1 += p2
        ans = min(ans, (-s1)*p1)
    print(ans)


if __name__ == '__main__':
    main()
