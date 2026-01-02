import copy

def stable_sort(A: list, N:int) -> list:
    """
    トランプのカードを整列しましょう。ここでは、４つの絵柄(S, H, C, D)と９つの数字(1, 2, ..., 9)から構成される計 36 枚のカードを用います。例えば、ハートの 8 は"H8"、ダイヤの 1 は"D1"と表します。
    バブルソート及び選択ソートのアルゴリズムを用いて、与えられた N 枚のカードをそれらの数字を基準に昇順に整列するプログラムを作成してください。アルゴリズムはそれぞれ以下に示す疑似コードに従うものとします。数列の要素は 0 オリジンで記述されています。
    5
    H4 C9 S4 D2 C3
    """

    def bubble_sort(A: list, N:int) -> list:
        """
        :A[N]: サイズがNの整数型配列。
        :i: 未ソートの部分の先頭を指すループ変数で、配列の先頭から末尾に向かって移動します。
        :j: 未ソートの部分の隣り合う要素を比較するためのループ変数で、Aの末尾であるN-1 から開始しi+1 まで減少します。
        """
        has_finished = True
        i = 0
        count = 0
        while has_finished and len(A) > 1:
            has_finished = False
            for j in reversed(range(i + 1, N)):
                if int(A[j][1]) < int(A[j - 1][1]):
                    # alter position
                    a, b = A[j - 1], A[j]
                    A[j - 1], A[j] = b, a
                    has_finished = True
                    count += 1
            i += 1

        return A

    def selection_sort(A: list, N:int) -> list:
        """
        :A[N]: サイズがNの整数型配列。
        :i: 未ソートの部分の先頭を指すループ変数で、配列の先頭から末尾に向かって移動する。
        :minj: 各ループの処理でi 番目からN-1 番目までの要素で最小のものの位置。j 未ソートの部分から最小値の位置（minj）を探すためのループ変数。
        """
        for i in range(0, N):
            minj = i
            for j in range(i, N):
                if int(A[j][1]) < int(A[minj][1]):
                    minj = j
            # alter position
            if i != minj:
                a, b = A[i], A[minj]
                A[i], A[minj] = b, a

        return A

    A_1 = A.copy()
    A_2 = A.copy()
    bubble_result = bubble_sort(A_1, N)
    selection_result = selection_sort(A_2, N)


    return bubble_result, selection_result


N = int(input())
A = list(input().split())

bubble_result, selection_result = stable_sort(A, N)

print(*bubble_result)
print("Stable")
print(*selection_result)
if bubble_result != selection_result:
    print("Not stable")
else:
    print("Stable")
