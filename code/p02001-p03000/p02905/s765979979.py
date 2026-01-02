# 解説 AC

# 参考1: https://twitter.com/rickytheta/status/1175412019006074880
# 参考2: https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2019-09-21agc-038

def make_prime_checker(n):
    # nまでの自然数が素数かどうかを表すリストを返す  O(nloglogn)
    is_prime = [False, True, False, False, False, True] * (n//6+1)
    del is_prime[n+1:]
    is_prime[1:4] = False, True, True
    for i in range(5, int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * (n//i-i+1)
    return is_prime

def make_modinv_list(n, mod=10**9+7):
    # 0 から n までの mod 逆元のリストを返す O(n)
    modinv = [0, 1]
    for i in range(2, n+1):
        modinv.append(mod - mod//i * modinv[mod%i] % mod)
    return modinv

def main():
    mod = 998244353
    max_A = 10**6
    N = int(input())
    A = list(map(int, input().split()))
    
    primes = [p for p, is_prime in enumerate(make_prime_checker(max_A)) if is_prime]  # max_A 以下の素数のリスト
    
    g = [0] * (max_A+1)
    for a in A:
        g[a] += a
    for p in primes:
        # 倍数集合の高速ゼータ変換みたいなやつ  O((max_A)loglog(max_A))
        # 参考: http://noshi91.hatenablog.com/entry/2018/12/27/121649
        # 大量に約数列挙みたいなことをするときはこれで高速化できる場合が多そう？（みんぷろ 2018 本戦 A - Uncommon など）
        for k in range(max_A//p, 0, -1):
            g[k] += g[k*p]
    
    # この時点で g[d] = Σ_{d|a} a  (A の要素のうち d の倍数であるものの総和)
    
    g = [v * v % mod for v in g]
    
    # この時点で
    # g[d] = (Σ_{d|a} a)(Σ_{d|b} b)
    #      = Σ_{(d|a)∧(d|b)} ab
    #      = Σ_{d | gcd(a,b)} ab
    
    # この式変形天才すぎないか？（これを使った一連の操作を gcd 畳み込み というらしい？）
    
    for p in primes:
        # 倍数集合の高速メビウス変換みたいなやつ  O((max_A)loglog(max_A))
    
        # for k in range(1, max_A//p+1):
        #     g[k] -= g[k*p]  # 包除原理ヤバい
    
        for k, g_kp in enumerate(g[p::p], 1):  # 高速化（ゼータ変換の方は途中で g が変化するので高速化できない）
            g[k] -= g_kp  # 包除原理ヤバい
    
    # この時点で g[d] = Σ_{gcd(a,b)=d} ab
    
    modinv_list = make_modinv_list(max_A, mod)
    ans = sum((gg * minv % mod for gg, minv in zip(g, modinv_list)))
    ans %= mod
    
    # この時点で
    # ans = Σ_d ( Σ_{gcd(a,b)=d} ab/d )
    #     = Σ_d ( Σ_{gcd(a,b)=d} lcm(a,b) )
    #     = Σ_a Σ_b lcm(a,b)
    
    ans -= sum(A)
    ans *= modinv_list[2]
    ans %= mod
    
    # この時点で ans = Σ_{i<j} lcm(a,b)
    
    print(ans)

main()
