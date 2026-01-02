#ABC167-E Colorful Blocks
"""
隣り合うブロックの組の個数がi個(i=0~k)であるときの組み合わせ数を求めていく。
まず、k=0の時を考えると、m=4の時、
res = 4*3**(n-1)となることがわかる。
次に、k>0のときは、
どれか2つのブロックを1つにつなぎ合わせると考えて、
res = 4*3**(n-1-i)
これに合わせて、どのブロックが接続するのかを考える必要があり、
どのブロックも右隣のブロックにのみ接続できると考えた場合、
接続できるブロックの個数はn-1個(一番右のブロックは接続先がない)
そこからi個選んで右のブロックにつなぐので、
n-1Ciとなる。
よって、k>0の場合の組み合わせ数は、
res = 4*3**(n-1-i)*(n-1)Ci
となる。
これを for i in range(0,k+1)だけ足し合わせたものが答え。
補足：
例えば3つのブロックを接続すると考えた場合、
2つをつなぎ合わせる場合と区別しそうだが、
「つなぐブロックの個数」はどちらでも同じになる。
更に、その時に全体の分割されたブロックの個数はn-i個で固定されるので、
m*pow(m-1,n-1-i)の部分が変わることもなく、
どの隣のブロックを選ぶかというのも隣接しても不都合がない。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,m,k = map(int,readline().split())
mod = 998244353
 
if m == 1:
    if k < n-1:
        print(0)
    else:
        print(1)
    exit()

def pow(n,p,mod=mod): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod

def factrial_memo(n=2*10**5,mod=mod):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
fact = factrial_memo()

def fermat_cmb(n, r, mod=mod): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod
ans = 0
for i in range(k+1):
    res = m*pow(m-1,n-1-i) #塊を含めて分けられるもの達
    ans += res*fermat_cmb(n-1,i)%mod
print(ans%mod)