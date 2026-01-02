def d_2017LikeNumber(Q, I):  # Q:クエリの数、I:探索区間の左端と右端
    def prime_list(M):
        # 0以上M以下の素数のリスト
        s = [True] * (M + 1)  # i番目の要素はiが素数ならTrue、非素数ならFalse
        for x in range(2, int(M**0.5) + 1):
            if s[x]:
                for i in range(x + x, len(s), x):
                    # 素数xの倍数は素数ではない
                    s[i] = False
        return s

    def calc_like2017(M, p):
        # i番目の要素が、1以上i以下の"2017に似た数"の個数となるようなリスト
        # 0番目は0と定義する
        # M以下の素数のリストpを予め作っておく必要がある
        c = [0] * (M + 1)
        for i in range(3, M + 1, 2):
            if p[i] and p[(i + 1) // 2]:
                c[i] += 1
        for i in range(3, M + 1):
            c[i] += c[i - 1]
        return c

    c = calc_like2017(10**5, prime_list(10**5))
    ans = ''
    for query in I:
        l, r = query[0], query[1]
        ans += '{}\n'.format(c[r] - c[l - 1])
    return ans[:-1]

Q = int(input())
I = [[int(i) for i in input().split()] for j in range(Q)]
print(d_2017LikeNumber(Q, I))