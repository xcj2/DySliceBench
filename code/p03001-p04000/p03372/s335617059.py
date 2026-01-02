def main():
    """
    1 <= N <= 10^5
    2 <= C <= 10^14
    1 <= x1 < x2 < ... < xN < C
    1 <= vi <= 10^9
    """
    N, C = map(int, input().split())
    X, V = zip(*(
        map(int, input().split())
        for _ in range(N)
    ))

    #part_point(N, C, X, V)
    editorial(N, C, X, V)


def editorial(N, C, X, V):
    rev_V = V[::-1]
    rev_X = tuple(map(lambda x: C-x, X[::-1]))

    a1 = solve_editorial(N, C, X, V)
    a2 = solve_editorial(N, C, rev_X, rev_V)
    ans = max(a1, a2)
    print(ans)


def solve_editorial(N, C, X, V):
    ans = 0
    
    # A側の累積和
    c1 = [0] * N
    c1[0] = V[0]
    for i in range(1, N):
        c1[i] = V[i] + c1[i-1]
    # 初期位置まで戻ったときの獲得カロリー
    d1 = [0] * N
    for i in range(N):
        # 食べた場所からすぐ帰る場合を計算しておく
        ans = max(c1[i] - X[i], ans)
        d1[i] = max(c1[i] - X[i] * 2, 0)
    # 寿司iまでの獲得カロリーの最大値
    e1 = [0] * N
    e1[0] = d1[0]
    for i in range(1, N):
        e1[i] = max(d1[i], e1[i-1])

    # B側の累積和
    rev_V = V[::-1]
    rev_X = tuple(map(lambda x: C-x, X[::-1]))
    c2 = [0] * N
    c2[0] = rev_V[0]
    for i in range(1, N):
        c2[i] = rev_V[i] + c2[i-1]

    # Bまでの獲得カロリーと、その1つ奥の寿司までのA側からの最大カロリー
    for i in range(N-1):
        y = max(c2[i] - rev_X[i], 0)
        ans = max(ans, e1[N-i-2] + y)

    return ans


def part_point(N, C, X, V):
    """
    円周すべてを通るパターンは最適ではない
        xN < C より
    時計回りにある寿司Aまで
    そこから初期位置まで
    最後に反時計回りにBまで
        OA * 2 + OB or
        OB * 2 + OA
    """
    # tupleの方が省memory (sys.getsizeof より)
    rev_V = V[::-1]
    rev_X = tuple(map(lambda x: C-x, X[::-1]))

    # 逆回りを計算し忘れてた
    a1 = solve_p(N, X, V, rev_X, rev_V)
    a2 = solve_p(N, rev_X, rev_V, X, V)

    ans = max(a1, a2)
    print(ans)


def solve_p(N, X, V, rev_X, rev_V):
    ans = 0
    for i in range(0, N):
        # Aまで
        a = sum(V[:i+1]) - X[i]
        ans = max(ans, a)
        # Oまで戻る
        a = max(a - X[i], 0)
        for j in range(N-i-1):
            # Bまで
            b = a + sum(rev_V[:j+1]) - rev_X[j]
            ans = max(ans, b)

    return ans


if __name__ == '__main__':
    main()
