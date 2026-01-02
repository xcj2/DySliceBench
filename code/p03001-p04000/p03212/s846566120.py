def main():
    """
    1 <= N  <= 10^9

    七五三数とは以下の条件を満たす正の整数
    十進法で表記したとき、
    数字 7, 5, 3 がそれぞれ 1回以上現れ、これら以外の数字は現れない
    """
    N = int(input())

    ans = f(N)
    print(ans)


def f(N):
    """
    Nの桁数がdのとき、d-1桁の数で753数であれば満たす
    上記d-1桁の753数に対して、
    753のそれぞれの数について
    桁追加をして、それがN以下であれば良い

    もっと簡単に考える
    d桁のとき並べる数字は3種類とその桁を使わないときに0埋めすると考えられる
    よって、並べ方の最大は (3+1)^9 = 262,144
        実際は実装上 349,525
    """
    d = len(str(N))
    ans = run_perm(N, d, [0, 3, 5, 7])
    # ans = TLE(N)

    return ans


def run_perm(N, d, types):
    """
    全列挙: TLE, 文字列処理がダメ

    http://www.geisya.or.jp/~mwm48961/kou3/onajimono1.htm
    による並べ方をやろうとしたけど断念
    """
    from collections import Counter
    a = [0] * d
    # nth = 0

    def perm(N, i, d, ans):
        # nonlocal nth
        # nth += 1

        if i == d:
            s = "".join(str(x) for x in a).lstrip("0")
            c = Counter(s)
            if c["0"] == 0 and \
                c["7"] >= 1 and \
                c["5"] >= 1 and \
                c["3"] >= 1 and \
                    int(s) <= N:

                ans += 1

            return ans

        for t in types:
            a[i] = t
            ans = perm(N, i+1, d, ans)

        return ans

    ans = perm(N, 0, d, 0)
    # print(nth)

    return ans


def TLE(N):
    ans = 0
    for i in range(357, N + 1):
        s = str(i)
        c7, c5, c3 = s.count("7"), s.count("5"), s.count("3")
        if len(s) == c7 + c5 + c3 and \
                c7 >= 1 and c5 >= 1 and c3 >= 1:
            ans += 1

    return ans


if __name__ == '__main__':
    main()
