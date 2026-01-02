import sys

change = False
debug = False


def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    """
    0 と 1 からなる文字列 S が与えられます。
    以下の操作を好きな回数繰り返すことで S の要素をすべて 0 にできるような、|S| 以下の最大の整数 K を求めてください。
    S の長さ K 以上の連続する区間 [l,r] を選ぶ(すなわち、r−l+1≥K が満たされる必要がある)。
    l≤i≤r なるすべての整数 i に対し、Si が 0 なら Si を 1 に、Si が 1 なら Si を 0 に置き換える。
    制約
    1≤|S|≤105
    Si(1≤i≤N) は 0 または 1 である
    """
    S = input()

    f(S)


def f(S):
    """
    最大となるKより、1つずつ変えるのは最後の手段
    ※K以上の反転可能であるため

    000: OK
    001, 110:  -> 100, 011
    010, 101:
      11を最終的に反転するように修正していく
        101: 1-3 all
        011: 1-2
        000: 2-3
    011, 100: 11を反転でOK

    0001 となっているとき
    K=3とすれば
    000 をまず反転、その後K+1まで反転すれば、初期状態からK+1番目のみ反転できる
    """
    n = len(S)
    ans = n

    # 反転確認
    table = str.maketrans('01', '10')
    for k in range(1, n):
        if S[k] == S[k - 1]:
            continue

        t = max(k, n - k)
        ans = min(ans, t)

        # 反転を利用して異なる部分を変更
        # 要素数の多い方を対称の異なる文字含めて反転

        # CPython3, PyPy: TLE
        if change:
            if t == k:
                S = S[:t].translate(table) + S[t:]
            else:
                S = S[:k] + S[k:].translate(table)

            if debug:
                print_err("t:", t, "k:", k, "S:", S, sep="\t")

    print(ans)

if __name__ == '__main__':
    main()
