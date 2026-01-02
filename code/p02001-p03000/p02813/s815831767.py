N = int(input())
P = [int(x) for x in input().split()]
Q = [int(x) for x in input().split()]
def get_order(N, src):
    MOD = 10**9+7

    bit = [0] * (N+1)
    def bit_add(a,w):
        x = a
        while x <= N:
            bit[x] += w
            x += (x & -x)

    def bit_sum(a):
        x = a
        ret = 0
        while x > 0:
            ret += bit[x]
            x -= (x & -x)
        return ret

    ans = fac = 1
    for i in range(N-1,-1,-1):
        a = src[i]
        ans += (bit_sum(a) * fac) % MOD
        bit_add(a,1)
        fac = (fac * (N-i)) % MOD

    return ans % MOD
print(abs(get_order(N,P)-get_order(N,Q)))
