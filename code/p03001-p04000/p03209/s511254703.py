def main():
    """
    input:
        1 <= N <= 50
        1 <= X <= レベル N バーガーの層の総数

    レベル L バーガー
        バン 1枚
        レベル L−1バーガー
        パティ 1枚
        レベル L−1バーガー
        バン 1枚
    この順に下から積み重ねたもの

    output:
        N! の約数のうち、七五数 は何個
        七五数とは約数をちょうど 75個持つ正の整数
    """
    N, X = map(int, input().split())

    ans = f(N, X)
    print(ans)


def layers(N):
    layer = [0] * (N + 1)
    layer[0] = 1
    p_layer = [0] * (N + 1)
    p_layer[0] = 1

    for i in range(1, N+1):
        layer[i] = 1 + layer[i-1] + 1 + layer[i-1] + 1
        p_layer[i] = p_layer[i-1] + 1 + p_layer[i-1]

    return layer, p_layer


def f(N, X):
    """
    差分は4から始まって2倍になる
    2^32 < layer 50 < 2^64

    下からX層を食べるので端から考える
    """
    layer, p_layer = layers(N)

    def patty(N, X):
        if N <= 0:
            return 0

        ans = 0
        # L下のバン
        if X >= 1:
            X -= 1
            # print("L下", N, X, ans)
            if X >= layer[N-1]:
                X -= layer[N-1]
                ans += p_layer[N-1]
                # print("L-1下バーガー", N, X, ans)
                if X >= 1:
                    X -= 1
                    ans += 1
                    # print("Lパティ", N, X, ans)
                    if X >= layer[N-1]:
                        X -= layer[N-1]
                        ans += p_layer[N-1]
                        # print("L-1上バーガー", N, X, ans)
                    else:
                        ans += patty(N-1, X)
            else:
                ans += patty(N-1, X)

        return ans

    ans = patty(N, X)
    return ans


if __name__ == '__main__':
    main()
