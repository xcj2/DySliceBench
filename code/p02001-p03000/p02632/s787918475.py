class ModCombination():
    def __init__(self, n, mod=998244353):
        self.mod = mod
        self.N = n
        fact = [1, 1] # 元テーブル
        ifact = [1, 1] #逆元テーブル
        inverse = [0, 1] #逆元テーブル計算用テーブル

        for i in range( 2, n + 1 ):
            fact.append( ( fact[-1] * i ) % mod )
            inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
            ifact.append( (ifact[-1] * inverse[-1]) % mod )
        
        self.fact = fact
        self.ifact = ifact
        self.inverse = inverse

    def nCr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.ifact[r] * self.ifact[n-r] % self.mod

    def nPr(self, n, r):
        if r < 0 or r > n:
            return 0
        return self.fact[n] * self.ifact[n-r] % self.mod

def main():
    K = int(input())
    S = input()
    MOD = 10 ** 9 + 7
    N = len(S)
    mc = ModCombination(N+K-1, MOD)

    # 方針
    # SがN文字のとき、
    # S+K文字の文字列からSの文字をどこに配置するか決め、配置を決めたら何パターンあるか計算し、その和をとる
    # 例: S = 'abc', K = 10 のとき, 配置を以下のようにしたとする
    # ***a**b*c****
    # aの前の***にはaを入れない、bの前の**にはbを入れない、cの前の*にはcを入れないようにする
    # 例えば、***ab*b*c**** のように、bの前の**にbを入れてしまうと、
    # ***ab***c**** でパターン数を数えるとき、***ab*b*c****もOKなパターンになるので、最終的に数え上げが重複してしまうため。
    
    # ***a**b*c****
    # この配置のときのパターン数は、
    # [a以外の25文字]^3 x [b以外の25文字]^2 x [c以外の25文字]^1 x [26文字]^4
    # = 26^[最後の文字(c)の後ろの*の数]  x 25^[最後の文字(c)より前にある*の数] 
    # となる。

    # このことから、Sの最後の文字の位置を決めて、それごとにパターン数を数え上げればいいとわかる。

    # Sの最後の文字の後ろの*の数をLとすると、最後の文字より前にある*の数はK-L個
    # 最後の文字以外のN-1文字とK-L個の*の配置パターンは、
    # (N-1+K-L)_C_(N-1) (n_C_r = 組み合わせ)
    # この配置パターンそれぞれに、26^L x 25^(K-L) のパターンがある

    ans = 0
    # Sの最後の文字の後ろの*の数
    for L in range(K+1):
        index_pattern = mc.nCr(N-1+K-L, N-1)
        char_pattern = pow(26, L, MOD) * pow(25, K-L, MOD) % MOD
        ans = (ans + index_pattern * char_pattern) % MOD

    print(ans)

if __name__ == '__main__':
    main()