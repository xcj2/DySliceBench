def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0: n, k, ret[i] = n//i, k+1, k+1
        if k > 0 or i == 97: sq = int(n**(1/2)+0.5)
        if i < 4: i = i * 2 - 1
        else: i, d = i+d, d^6
    if n > 1: ret[n] = 1
    return ret
def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)
def o_divisors(N):
    return [a for a in divisors(N) if N//a % 2 and a < N]
    
N = int(input())
T = input()
P = 998244353
ods = o_divisors(N)

bt = int(T, 2)
c = 0
ans = 0
L = []
for k in ods:
    tt = T[:k]
    tt_ = tt.replace("0", "2").replace("1", "0").replace("2", "1")
    
    ttf = tt + (tt_ + tt) * ((N//k-1)//2)
    aa = int(tt, 2)
    if int(ttf, 2) <= bt:
        aa += 1
    for l, cc in L:
        if k % l == 0:
            aa -= cc
    L.append((k, aa))
    c += aa
    ans += k*2*aa
        
ans = (ans + 2 * N * (bt - c + 1)) % P
print(ans)

