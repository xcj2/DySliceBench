#!/usr/bin/env python3
"""
ソートテク関連の基本的な関数の詰め合わせ (命名は C++ STL algorithm による)


stable_partition(seq, func):
    O(n)
    空間計算量も O(n)
    述語が True を返す全ての要素が、述語が False を返す全ての要素よりも前になるようにシーケンスを並び替える (破壊、安定)


nth_element(seq, k, begin, end):
    O(n)
    E = seq[k] とする
    特定の要素 E よりも小さい全ての要素が E よりも前になり、 E 以上の全ての要素がEよりも後になるように seq[begin:end] を並び替える (破壊、不安定)
    heapq の nlargest とは異なるので注意


ith_order_statistic(seq, i, begin, end):
    O(n)
    nth_element を用いて (seq[begin:end] に存在することがわかっている) i 番目の順序統計量を求める (i = 0, 1, ..., n-1)


simple_quick_sort(seq, begin, end):
    O(nlgn)
    nth_element を用いて seq[begin:end] をソートする (破壊、不安定)


modified_merge_sort(seq, begin, end):
    O(nlgn)
    _modified_merge を用いて seq[begin:end] をソートする (非破壊、安定)
    転倒数とソート済み配列を返す


count_inversion(seq):
    O(nlgn)
    modified_merge_sort を用いて seq の転倒数を求める
    (転倒数: seq[i] > seq[j] (i < j) なる (i, j) の組み合わせの数のこと)
"""


import random
from typing import TypeVar, Callable, List, Tuple, Union
T = TypeVar('T')
Num = Union[int, float]




def _modified_merge(left: List[Num], right: List[Num]) -> Tuple[int, List[Num]]:
    """
    ソート済み配列 left, right を受け取り、全体のソート済み配列を生成する (O(n))
    マージの過程で転倒数をメモして返す

    Args:
        left (list): ソート済み
        right (list): ソート済み

    Returns:
        inv (int): 転倒数
        sorted_list (list): ソート済み
    
    Examples:
        >>> _modified_merge([1, 5, 7], [2, 3, 3])
        (6, [1, 2, 3, 3, 5, 7])
    """
    sorted_list = []
    i, j, inv = 0, 0, 0
    buf_1 = left[:] + [float('inf')]
    buf_2 = right[:] + [float('inf')]
    for _ in range(len(left) + len(right)):
        if buf_1[i] < buf_2[j]:
            sorted_list.append(buf_1[i])
            i += 1
        else:
            sorted_list.append(buf_2[j])
            j += 1
        inv += 1
    return inv, sorted_list


def modified_merge_sort(L, begin, end):
    """
    L[begin:end] を 非破壊的かつ安定にマージソートする (O(nlgn))
    マージソートの過程で転倒数をメモして返す

    Args:
        L (list)
        begin, end (int)
    
    Returns:
        inv (int): 転倒数
        sorted_list (list): ソート済み
    
    Examples:
        >>> modified_merge_sort([3, 5, 2, 1, 0], 0, 5)
        (9, [0, 1, 2, 3, 5])
    """
    if end - begin == 1:
        return 0, [L[begin]]
    mid = (begin + end) // 2
    left_inv_cnt, left = modified_merge_sort(L, begin, mid)
    right_inv_cnt, right = modified_merge_sort(L, mid, end)
    merge_inv_cnt, sorted_list = _modified_merge(left, right)
    return left_inv_cnt + right_inv_cnt + merge_inv_cnt, sorted_list



# verified @AOJ ALDS1_5_D
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D&lang=ja
def count_inversion(L):
    """
    modified_merge_sort() を用いて L の要素の転倒数を求める (O(nlgn))

    Examples:
        >>> count_inversion([1, 9, 2, 7, 5, 6, 4, 8, 3, 0])
        26
    """
    cnt, _ = modified_merge_sort(L, 0, len(L))
    return cnt



if __name__ == "__main__":
    n = int(input())
    L = list(map(int, input().split()))
    num, seq = modified_merge_sort(L, 0, n)
    print(*seq, sep=' ')
    print(num)    
