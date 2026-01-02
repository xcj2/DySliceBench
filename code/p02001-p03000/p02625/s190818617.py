import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 10**9 + 7
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]

    N,M = LI()

    f = [1]
    r = [1]
    c = 1
    for i in range(1, M + 1):
        c = (c * i) % MOD
        f.append(c)
        r.append(pow(c, MOD - 2, MOD))

    def comb(n, k):
        return (f[n] * r[k] * r[n - k]) % MOD
    def perm(n, k):
        return (f[n] * r[n-k]) % MOD


    ans = 0
    for i in range(N+1):
        ans = (ans + ((-1)**i) * comb(N,i) * perm(M,i) * (perm(M-i,N-i) ** 2)) % MOD
    print(ans)



if __name__ == '__main__':
    main()