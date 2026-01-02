import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    MOD = 998244353
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    N = NI()
    dat = [LI() for _ in range(N)]
    dat.sort()
    yo = [y for _,y in dat]
    yo.sort()

    up = [0] * N
    dw = [0] * N

    bit = [0] * (N+1)

    def bit_add(i):
        while i <= N:
            bit[i] += 1
            i += i & -i

    def bit_sum(i):
        ret = 0
        while i > 0:
            ret += bit[i]
            i -= i & -i
        return ret

    for i in range(N):
        x,y = dat[i]
        y = bisect.bisect_left(yo,y) + 1
        up[i] = bit_sum(y)
        bit_add(y)

    bit = [0] * (N+1)
    for i in range(N-1,-1,-1):
        x,y = dat[i]
        y = bisect.bisect_left(yo,y) + 1
        dw[i] = bit_sum(y)
        bit_add(y)

    ans = N * pow(2,N-1,MOD)
    for i in range(N):
        a = i - up[i]
        b = up[i]
        c = N-(i+1) - dw[i]
        d = dw[i]
        pa = pow(2,a,MOD)
        pb = pow(2,b,MOD)
        pc = pow(2,c,MOD)
        pd = pow(2,d,MOD)
        pad = pow(2,a+d,MOD)
        pbc = pow(2,b+c,MOD)
        p = (pad-1) - (pa-1) - (pd-1)
        q = (pbc-1) - (pb-1) - (pc-1)
        x = p * pbc
        y = q * pad
        z = p * q
        ans = (ans + x + y - z) % MOD
    print(ans)

if __name__ == '__main__':
    main()