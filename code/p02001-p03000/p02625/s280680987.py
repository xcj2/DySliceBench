#ABC172-E NEQ
"""
玉：各要素(1~m)(区別あり)
箱：配列の格納場所(1~n)(区別あり)
条件：全射かつ、任意のiにおいてAi != Biとなるような2つの組み合わせ
問題の余事象は
Ai = Biとなるような要素の選び方
となる。
全事象(mCn ^2)からこれを引けば良いので、
包除原理を用いて、
A0 = B0となる場合
A1 = B1となる場合…
を数え上げる。

0~n個までの重複要素について、
-1^i *(n箱からi個選んで重複させる*その時のm個の整数からの選び方はmPi)*残りのn-i個はm-i個から任意に選ぶ(m-iPn-i)^2
を実装する
n箱からi箇所選ぶのは区別しなくて良いが、(その選び方に区別は無いため)
それ以外の、その場所にどの数字を入れるかはちゃんと区別しないといけないため順列になり、
また、残りの箇所もAとBの配列それぞれについて(ここが^2)整数を区別して(順列)自由に選べることに注意。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
mod = 10**9+7
n,m = map(int,readline().split())
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

def factrial_memo(n=10**6,mod=mod):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact

fact = factrial_memo()

def permutation(n,r): #nPr
    return fact[n]*pow(fact[n-r],mod-2)%mod
def combination(n,r): #nCr
    return permutation(n,r)*pow(fact[r],mod-2)%mod
    #return fact[n]*pow(fact[n-r],mod-2)*pow(fact[r],mod-2)
def homogeneous(n,r): #nHr
    return combination(n+r-1,r)%mod
    #return fact[n+m-1]*pow(fact[n-1],mod-2)*pow(fact[r],mod-2)

ans = 0
for i in range(n+1):
    #print(combination(n,i)*permutation(m,i)*pow(permutation(m-i,n-i),2)%mod)
    ans += pow(-1,i)*combination(n,i)*permutation(m,i)*pow(permutation(m-i,n-i),2)%mod
    ans %= mod

print(ans)