# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C

最長共通部分列
"""


c = []
def prep_array(X, Y):
    global c
    """ 値が0の2次元配列を用意する。サイズは入力データの最大値を想定して縦横(1000+1)以上必要。 """
    # from array import array
    # c = [array('I', [0] * (len(X)+1)) for _ in range(len(Y)+1)]  #  arrayで用意
    c = [[0]*(len(Y)+2) for _ in range(len(X)+2)] #  リストで用意
    return c


def check_max(array):
    """ 2次元配列の中の最大の値を返す """
    max_lcs = 0
    for row in array:
        temp_max = max(row)
        if temp_max > max_lcs:
            max_lcs = temp_max
    return max_lcs


def calc_lcs4(X, Y, c):
    """
    Y[j]のアクセス方法を変更
    リストの値を一旦変数に保存するように変更
    最長共通部分長を関数内で計算するように変更
    4/5 のテストデータを使用してプロファイリングすると実効時間は 5.6秒
    """
    X = ' ' + X
    Y = ' ' + Y
    m = len(X)
    n = len(Y)
    max_lcs = 0

    pre_row = c[0]
    for i in range(1, m):
        row = c[i]
        XX = X[i]
        for j, YY in enumerate(Y):
            if XX == YY:
                pr_j1 = pre_row[j - 1]
                row[j] = pr_j1 + 1
                if pr_j1+1 > max_lcs:
                   max_lcs = pr_j1 + 1
            else:
                pr_j = pre_row[j]
                r_j1 = row[j-1]
                if pr_j >= r_j1:
                    row[j] = pr_j
                else:
                    row[j] = r_j1
        pre_row = row
    return max_lcs


if __name__ == '__main__':
    # データの入力
    num = int(input())
    #f = open('input.txt')
    #num = int(f.readline())

    for _ in range(num):
        X = input().strip()
        Y = input().strip()

        # 処理の実行
        result = calc_lcs4(X, Y, prep_array(X, Y))

        # 結果の表示
        print(result)


