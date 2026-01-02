"""マージソートを用いて安定かどうかを確認する。"""

from typing import List, Tuple
import math
import sys


class sort_object:
    """ソート対象のオブジェクト。必要に応じてプロパティやメソッドを増やす。"""

    def __init__(self, value: int, inf1='', inf2=''):
        self.value = value
        self.inf1 = inf1

    def set_value(self, value: int):
        self.set_value = value

    def get_value(self):
        return self.value

    def set_inf1(self, inf1):
        self.inf1 = inf1

    def get_inf1(self):
        return self.inf1

    def set_inf2(self, inf2):
        self.inf2 = inf2

    def get_inf2(self):
        return self.inf2


def merge(A: List[sort_object], left: int, mid: int, right: int) -> None:

    left_list = A[left:mid]
    right_list = A[mid:right]
    left_list.append(sort_object(sys.maxsize))
    right_list.append(sort_object(sys.maxsize))

    i = 0  # left_listのインデックス
    j = 0  # right_listのインデックス
    for k in range(left, right):
        if left_list[i].get_value() <= right_list[j].get_value():
            A[k] = left_list[i]
            i += 1
        else:
            A[k] = right_list[j]
            j += 1


def merge_sort(A: List[sort_object], left: int, right: int) -> int:
    if left + 1 < right:
        mid = math.floor((left + right) / 2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


def partition(A: List[sort_object], p: int, r: int) -> int:
    """パーティション

    A[p, ..., r]を、A[p, ..., q-1]とA[q+1, ..., r]二分割する。
    A[p, ..., q-1]の各要素は A[q]以下とする。
    A[q+1, ..., r]の各要素は A[q]より大きくする。

    Args:
        A (List[int]): 分割対象のリスト
        p (int): 分割対象のリストの先頭のインデックス
        r (int): 分割対象のリストの最後のインデックス

    Returns:
        int: q
    """
    tmp = A[r].get_value()
    i = p - 1
    for j in range(p, r):
        if A[j].get_value() <= tmp:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A: List[sort_object], p: int, r: int) -> None:
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return


n = int(input())
cards_1 = []
for _i in range(n):
    pic, num = map(str, input().split())
    num = int(num)
    cards_1.append(sort_object(num, pic))
cards_2 = [i for i in cards_1]

quick_sort(cards_1, 0, n - 1)
merge_sort(cards_2, 0, n)

if cards_1 == cards_2:
    print('Stable')
else:
    print('Not stable')
for c in cards_1:
    print(c.get_inf1(), c.get_value())

