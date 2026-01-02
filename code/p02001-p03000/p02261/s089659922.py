# ALDS1_2_C.
# バブルソートと選択ソートの安定性。
from math import sqrt, floor

class card:
    def __init__(self, _str):
        # S3とかH8をもとに初期化。
        self.kind = _str  # 出力用。
        self.suit = _str[0]
        self.value = int(_str[1])

def cardinput():
    # カードの配列からオブジェクトの配列を生成。
    a = input().split()
    cards = []
    for i in range(len(a)):
        cards.append(card(a[i]))
    return cards

def show(a):
    # 配列の中身を出力する。
    _str = ""
    for i in range(len(a) - 1):
        _str += a[i].kind + " "
    _str += a[len(a) - 1].kind
    print(_str)

def bubble_sort(a):
    # aをバブルソートする(交換回数をreturnする)。
    count = 0
    for i in range(1, len(a)):
        k = i - 1
        while k >= 0:
            # a[i]を前の数と交換していき、前の方が小さかったら止める。
            if a[k].value > a[k + 1].value:
                a[k], a[k + 1] = a[k + 1], a[k]
                count += 1
            else: break
            k -= 1
    return count

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
            if a[j].value < a[minj].value: minj = j
        if a[i].value > a[minj].value: count += 1; a[i], a[minj] = a[minj], a[i]
    return count

def main():
    N = int(input())
    cards = cardinput()
    # バブルソートは安定。同じvalueなら団子のようにくっつくから。
    # 選択ソートは交換が飛び越えるので不安定。よって、
    # バブルの結果と比較すれば安定か不安定かが分かる。
    _copy = [cards[i] for i in range(N)]

    bubble_sort(cards)
    selection_sort(_copy)

    show(cards)
    print("Stable")
    show(_copy)

    is_stable = True
    for i in range(N):
        for j in range(i + 1, N):
            if _copy[i].value != _copy[j].value: continue
            if _copy[i].suit != cards[i].suit: is_stable = False; break
    if is_stable: print("Stable")
    else: print("Not stable")

if __name__ == "__main__":
    main()
