mod = 10**9+7 #出力の制限
def pow_r(x, n):
    """
    O(log n)
    """
    if n == 0:  # exit case
        return 1
    if n % 2 == 0:  # standard case ① n is even
        return pow_r((x ** 2)%1000000007 , n // 2) % mod
    else:  # standard case ② n is odd
        return x * pow_r((x ** 2)%1000000007, (n - 1) // 2) % mod

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    g1=1
    r = min(r, n-r)
    for i in range(n-r+1,n+1):
        g1*=i
        g1%=mod



    return g1 * g2[r] % mod


g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
def getgen(N):
    for i in range( 2, N + 1 ):

        inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
        g2.append( (g2[-1] * inverse[-1]) % mod )




def resolve():
    n,a,b=map(int,input().split())
    sm=pow_r(2,n)-1
    getgen(max(a,b))
    aa=cmb(n,a,mod)
    bb=cmb(n,b,mod)

    sm-=aa

    if sm<0:
        sm+=mod
    sm-=bb
    if sm<0:
        sm+=mod
    
    print(sm)
    







if __name__ == "__main__":
    resolve()
