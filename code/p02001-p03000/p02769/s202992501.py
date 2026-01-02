ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))
n,k = mi()
#a^-1 (mod P)
mod = 10 ** 9 +7
def modinv(a, mod=10**9+7):
    return pow(a, mod-2, mod)

def combination(n, r, mod=mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

'''
ここは任意
'''

g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

#  これは計算量rでncr mod p を求められる。
def combination2(n, r, mod=10**9+7):
    r = min(r, n-r)
    res = 1
    for i in range(r):
        res = res * (n - i) * modinv(i+1, mod) % mod
    return res

for i in range( 2, n + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def main():
    if k >= n -1:
        ans = combination2(2*n -1,n-1)
        print(ans)
    else:
        ans = 1
        for i in range(1,k+1):
            zero_comb = combination(n,i)
            cou = combination(n-1,n-i-1) * zero_comb % mod
            #print(cou)
            ans = (ans +cou) % mod
        print(ans)
main()
