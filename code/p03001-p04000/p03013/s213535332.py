import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7


def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限。素数しか使用不可。
N = 2*10**5
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

# need to calculate factorials to n+k-1
def combinations_with_repetition(n, k):
    return cmb(n+k-1, k, mod)

def num_of_pattern(n):
    sum_of_pattern = 0
    if n%2 == 1:
        for k in range(0,n,2):
            sum_of_pattern += combinations_with_repetition(((n-k)//2)+1, k)
        return sum_of_pattern % mod
    else:
        for k in range(1,n,2):
            sum_of_pattern += combinations_with_repetition(((n-k)//2)+1, k)
        return sum_of_pattern % mod

def main(): 
    N, M = LI()
    a_li = [-1]
    prev = INF
    for _ in range(M):
        now = II()
        if prev+1 == now:
            print(0)
            return
        elif prev == now:
            continue
        prev = now
        a_li.append(now)
    a_li.append(N+1)

    ans = 1
    for i in range(len(a_li)-1):
        ans *= num_of_pattern(a_li[i+1] - a_li[i] - 1)
        ans %= mod

    print(ans)

main()