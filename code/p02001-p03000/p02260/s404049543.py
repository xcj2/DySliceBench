# ALDS_2_B.
# バブルソート。
from math import sqrt, floor

def intinput():
    a = input().split()
    for i in range(len(a)):
        a[i] = int(a[i])
    return a

def show(a):
    # 配列の中身を出力する。
    _str = ""
    for i in range(len(a) - 1):
        _str += str(a[i]) + " "
    _str += str(a[len(a) - 1])
    print(_str)

def selection_sort(a):
    # 選択ソート。その番号以降の最小値を順繰りにもってくる。
    # 交換回数は少ないが比較回数の関係で結局O(n^2)かかる。
    count = 0
    for i in range(len(a)):
        # a[i]からa[len(a) - 1]のうちa[j]が最小っていうjを取る。
        # このときiとjが違うならカウントする。
        # というかa[i]とa[j]が違う時カウントでしたね。
        minj = i
        for j in range(i, len(a)):
            if a[j] < a[minj]: minj = j
        if a[i] > a[minj]: count += 1; a[i], a[minj] = a[minj], a[i]
    return count

def main():
    N = int(input())
    A = intinput()
    count = selection_sort(A)
    show(A); print(count)

if __name__ == "__main__":
    main()
