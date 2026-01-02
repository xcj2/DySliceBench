import sys
def input(): return sys.stdin.readline().strip()
sys.setrecursionlimit(10 ** 9)


"""
ABC160-Fの解説放送での実装をPythonで焼きなおしてみました。
内訳：
    class Combination : mod付きの組み合わせの計算用クラス
    class DP : 木DPを行うためのクラス（本問用に特殊化）
    dfs(v, p=-1) : 頂点v以下の部分木に対してdpした結果を返す
    bfs(v, p=-1) : 頂点vに入ってくるdp値の総和を取り、頂点vの子供に親からのdp値を渡す
"""

class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n-r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n+1):
            fac.append(fac[i-1] * i % self.mod)
            facinv.append(facinv[i-1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            modinv[i] = self.mod - self.mod//i * modinv[self.mod%i] % self.mod
        return modinv

# 早速グローバル変数として用意しておく
cmb = Combination(2 * 10 ** 5)


class DP:
    """
    木DPをする準備として、dpの値と木のサイズを両方保持するクラスを定義する。
    さらに演算子オーバーロードにより足し算記号でdpの値の更新（今回は組み合わせ含む掛け算）と
    木のサイズの合算を同時にやってくれるようにする。
    dp計算は全てmodを取ることに注意。
    """
    def __init__(self, m_dp=1, m_t=0, mod=10**9+7):
        self.dp = m_dp
        self.t = m_t
        self.mod = mod
    
    def __iadd__(self, other):
        """
        a = DP(3, 2); b = DP(4, 5)として
        a += bによりa = DP(12, 7)みたいになる。
        二つの木を合わせるために新しくつける根はまだ足していないことに注意。
        """
        self.dp *= other.dp * cmb(self.t + other.t, self.t)
        self.dp %= self.mod
        self.t += other.t
        return self
    
    def __sub__(self, other):
        """
        引き算も同様にオーバーロード（ただしこっちは二項演算）。
        また、こちらはbfsで親の木のdp値を送ることを念頭においていることに注意。
        """
        dp = self.dp * pow(other.dp * cmb(self.t - 1, other.t), self.mod - 2, self.mod) # dp = self.dp / other.dp * cmb(self.t - 1, other.t)
        t = self.t - other.t
        return DP(dp, t)
    
    def addRoot(self):
        self.t += 1
        return self
    
    def subroot(self):
        self.t -= 1
        return self



def main():
    N = int(input())
    repn = [[] for _ in range(N)]
    mod = 10**9+7

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        repn[a].append(b)
        repn[b].append(a)

    """
    まずは頂点0を根として木DPをする、すなわち頂点0に数字1を書き込んだ場合の
    残りの数の書き込み方の場合の数を計算する。
    """

    # 最初の木DPの途中経過を記録する配列を準備
    # dp[v][i] = (頂点vのi番目の子を根とする部分木から頂点vに渡されるdp値)
    dp = [[DP() for u in repn[v]] for v in range(N)]
    # dpSum[v] = (頂点vの子供を根とする部分木からそれぞれ頂点vに渡されるdp値の総和)
    dpSum = [DP() for _ in range(N)]

    def dfs(v, p=-1):
        """
        dfsというよりは木DPをした結果を返す関数。

        根がvの部分木（頂点pはvの親として含めない）のdp結果を返すが、
        そのためにvの各子供に対する部分木dpの結果を足し合わせて、
        最後に木のサイズを1(v自身の分)だけ増やしている。

        v自身が葉ノードの場合はDPクラス内で既に初期化が済んでいることに注意。
        """
        for i, u in enumerate(repn[v]):
            if u == p:
                continue
            dp[v][i] = dfs(u, v)
            dpSum[v] += dp[v][i]
        return dpSum[v].addRoot()

    dfs(0)
    # この時点で各dpSum[v]には、子供らのdp値を総和した値と、頂点vを含む木のサイズが記録される
    # for i in range(N):
    #     print("dpSum[{}]=[{}, {}]".format(i, dpSum[i].dp, dpSum[i].t))

    """
    次に全方位木DPのためのbfsを行う。
    全方位木そのもののアルゴリズムは解説放送を参照。
    あえてポイントを述べるとすれば、
        1. 木の各辺の向きが、部分木と１対１対応する。
        2. dfs時点で各辺の根に上がる向きの部分木dpは記録済み
        3. 逆向きの辺のdp値は、全ての隣接辺に対して入ってくる向きの
        　　dp値がわかっている頂点（例えば根）に関してならdp値の総和を
        　　考えることで出ていく向きのdp値がO(1)で求まる。
        4. これを隣接する頂点ごとに計算すればよい。
    """

    def bfs(v, dpP=DP(), p=-1):
        """
        頂点vからのbfsというかdfsで求めたdp値の逆伝搬（出ていく方のdp値）の計算を行う。
        dpPは頂点vの親から来る部分木のdp値。

        まず親から来る部分木のdp値を加えることで、頂点vに隣接する全ての辺から入ってくる
        dp値の総和を完成させる。
        
        このときdpSum[v]自体が頂点vを含んでしまうとdp計算で木のサイズを使う際に狂いが生じるので、
        一旦頂点vを除いたうえでdpPを加えて、その後頂点vを戻す（これで頂点vに対する解は求まった）。
        """
        
        if p != -1:
            dpSum[v].subroot()
            dpSum[v] += dpP
            dpSum[v].addRoot()

        # 次に頂点vのそれぞれの子（頂点u）に対して、頂点uを主役と見たときの親からのdp値を渡す。、
        for i, u in enumerate(repn[v]):
            if u == p:
                dp[v][i] = dpP
            else:
                d = dpSum[v] - dp[v][i]
                bfs(u, d, v)
    
    bfs(0)
    for i in range(N):
        # print("dpSum[{}]=[{}, {}]".format(i, dpSum[i].dp, dpSum[i].t))
        print(int(dpSum[i].dp))



if __name__ == "__main__":
    main()