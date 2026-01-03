def main():
    """
    カレンダーらしいもの: 7列…

    3x3の和: 2列目x3
    2列目の平均: (2,2)
    より,(2,2)*9

    11で割った余り
    9............13
    16...........20
    ...

    9,10,0,1,2
    5,6, 7,8,9

    [以下、解説の(自分用の)補完]
    9x ≡  k mod 11
     x ≡ 5k mod 11 ?

    わからんーとTweetしたら, 引用で解説されてた(感謝)
    1. https://twitter.com/hogeover30/status/995618880830636032
    2. https://mathtrain.jp/mod

        45x     ≡ 5k mod 11 (両辺等倍しても剰余は変わらない, 性質3)
        44x + x ≡ 5k mod 11 (求めたいxと 11で割り切れる倍数に分解, 性質1)
              x ≡ 5k mod 11

    範囲の変更
        7i + j - 7 (2<=i<=n-1, 2<=j<=6)
        7i + j + 9 (0<=i<=n-3, 0<=j<=4)
            7*2 + 1*2 = 16
            16 - 7 = 9

    7i に着目(入力例4, n=100, k=8)
        j=0: 7i+9  ≡ 5k ≡ 40 (mod 11) => 7i ≡ 9 (mod 11) ※1
        j=1: 7i+10 ≡ 5k ≡ 40 (mod 11) => 7i ≡ 8 (mod 11) ※2
            ※1: 40-9 (31) mod 11 = 9 より (性質2)
            ※2: 40-10(30) mod 11 = 8 より

            i={6,17,28,39,50,61,72,83,94}
            i={9,20,31,42,53,64,75,86,97}

    j固定: i = 11q + r
        1: r=6
        2: r=9
    結局、規則はなんとなく分かるが証明しろと言われると説明できない
    """
    n, k = map(int, input().split())

    # part1(n, k)
    # f2(n, k)
    editorial(n, k)


def f2(n, k):
    """規則をなんとなく見つけた場合
    """
    table = []
    for i in range(2, 2+11):
        table.append(
            [(7*i + j - 7) * 9 % 11 for j in range(2, 6+1)]
        )

    # 最初と最後の1行ずつ不要
    n -= 2
    # 11ごとに1つ解が存在し5列分
    ans = n // 11 * 5
    # 余った行ごとに残りの判定
    x = n % 11
    for i in range(x):
        for j in range(5):
            if table[i][j] == k:
                ans += 1

    print(ans)


def editorial(n, k):
    ans = 0
    # 列ごと: 2行目2-6列目
    for j in range(2, 6+1):
        rownum = 0
        for i in range(2, n):
            s = (i * 7 + j - 7) * 9
            if s % 11 == k:
                rownum = i
                break

        if rownum == 0:
            continue

        # 11行ごとに余りkになるため、見つかった基準の分の+1
        # 最後の1行不要, rownumずらしておく
        ans += 1
        ans += (n - 1 - rownum) // 11

    print(ans)


def part1(n, k):
    ans = 0

    for i in range(1, n-3+2):
        for j in range(1, 5+1):
            s = 0
            for y in range(3):
                for x in range(3):
                    s += 7*(i+y) + (j+x) - 7
            # print(i, j, s, sep="\t")
            if s % 11 == k:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
