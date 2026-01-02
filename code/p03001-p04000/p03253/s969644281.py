def ord(N,n):#N,nは正の整数、Nで割り切れる回数、許容はN^1000
    if n%N!=0:
        return 0
    else:
        return 1+ord(N,n//N)

def get_sieve_of_eratosthenes_new(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

primelist=get_sieve_of_eratosthenes_new(32*(10**2))

def cmb(n, r, mod):#コンビネーションの高速計算　
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


def main():
    N,M=map(int,input().split())
    product=1
    for i in range(0,len(primelist)):
        product=(product*cmb(ord(primelist[i],M)+N-1,N-1,mod))%mod
        M=M//primelist[i]**ord(primelist[i],M)
    if M!=1:
        product=(product*N)%mod
    print(product)

if __name__ == '__main__':
    main()
