
def resolve():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aは偶数。2*Bと書ける。少数をなくすため, B*(2p + 1)と式変形
    # 2を使用した為、2で割る
    B = [a//2 for a in A]

    # X = B[k] * (2p + 1)
    # これを見てみると、B[k]の奇数倍の数が作られることになる。
    # 公倍数は最小公倍数の倍数となるという性質がある。
    # 全部の数の最小公倍数を取って、M÷最小公倍数をすると答えが得られる。
    def solve():
        lc = 1
        for i in range(N):
            lc = lcm(lc, B[i])

        # 変形式より、XはB*奇数倍されないといけないX//B[k] == (2p+1)
        # なので、偶数になるとダメ
        for i in range(N):
            if (lc//B[i]) % 2 == 0:
                return 0
        ans = M//lc
        ans = (ans+1)//2
        return ans

    print(solve())

if __name__ == "__main__":
    resolve()