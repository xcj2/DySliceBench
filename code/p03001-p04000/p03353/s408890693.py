def main():
    """
    1<=|s|<=5,000
    1<=K<=5
    """
    s = input()
    K = int(input())

    part(s, K)


def f(s, K):
    """
    K=1, sorted(s)[0]
    K=2, s[min_idx:min_idx+2]
        aabbaac

        min:a, next: aa
        aab<aac
    1-5文字: すべて異なる文字列なら1文字でよい

    minから5種類存在するなら不要
        K個以上存在する
    a: min
    aaaaa: 5th(aa,aaa,aaaaがあれば)

    abced: 完了
    babcd: 途中にaがあるから未完
     abcde: 完了,ただしaaaaaとかあったらNG
    """
    pass


def part(s, K):
    #s = "abcde" * 1000
    n = len(s)
    ss = set()
    for i in range(n):
        # 最初なぜかn文字まで繰り返していたが、辞書順を考えれば不要
        for j in range(i, i+K):
            subs = s[i:j+1]
            # print(subs, i, j, sep="\t")
            ss.add(subs)

    ans = sorted(ss)[K-1]
    print(ans)


if __name__ == '__main__':
    main()
