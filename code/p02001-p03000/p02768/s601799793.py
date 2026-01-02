p = 10 ** 9 + 7
N = (10 ** 5)*2 +10  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

def cmb(n, r, p):
    mm = 1
    for i in range(n,n-r,-1):
        mm *= i
        mm %= p
    return mm*factinv[r]%p



def pwr(n,k): #nのk乗高速版 n^k
    mod = 10**9+7
    memo = chng2(k)
    lng = len(memo)

    li = [0 for i in range(lng-1)]
    li[0] = 1
    
    a = 2
    ans = 1
    for i in range(1,lng-1):
        li[i] = a
        a *= a
        a %= mod 
 
    for i in range(1,lng-1):
        if memo[-i]=='1':
            ans *= li[i]%mod

    return ans%mod

def chng2(n): #10進数nを2進数に変換(配列)
    ans = list(bin(n))
    return ans


mod = 10**9+7
N,A,B = map(int,input().split())
mm1 = pwr(2,N)
mm2 = cmb(N,A,mod)
mm3 = cmb(N,B,mod)

ans = mm1-mm2-mm3-1
if ans < 0:
    ans += mod

print(ans%mod)
