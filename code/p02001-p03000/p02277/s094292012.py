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




import random
from typing import TypeVar, Callable, List, Tuple, Union
T = TypeVar('T')
Num = Union[int, float]



def nth_element(L: List[Num], pivot_ind: int, begin: int=-1, end: int=-1, key=lambda x: x) -> int:
    """
    pivot = L[pivot_ind] とする。 'pivot 未満の要素 ... pivot ... pivot 以上の要素' となるよう L を破壊的に並び替える。(O(n))
    最後に基準値の pivot がおさまった場所のインデックスを返す。
    begin <= pivot_ind < end の要請はあるが、begin, end の指定により L[begin:end] に対象を絞り L[pivot_ind] 未満 / 以上に並べ替えることもできる。

    Args:
        L (list)
        pivot_ind (int)
        begin, end (int): L の [begin, end) 半開区間を考える。デフォルトでは L[0:n] となる

    Returns:
        int: 最後に基準値の pivot がおさまった場所のインデックス

    Examples:
        >>> seq = [1, 9, 2, 7, 5, 6, 4, 8, 3, 0]
        >>> nth_element(seq, 4)
        5
        >>> seq
        [1, 2, 0, 4, 3, 5, 7, 8, 9, 6]
        >>> nth_element(seq, 3, begin=3, end=9)
        4
        >>> seq
        [1, 2, 0, 3, 4, 5, 7, 8, 9, 6]
    """
    if begin == -1 and end == -1:
        begin, end = 0, len(L)
    if not begin <= pivot_ind < end:
        raise RuntimeError(f"nth_element(): pivot_ind should be begin <= pivot_ind < end. got pivot_ind={pivot_ind}, begin={begin}, end={end}.")

    # [begin]...[end] が対象範囲である
    end -= 1
    pivot = L[pivot_ind]
    L[pivot_ind], L[end] = L[end], L[pivot_ind]
    # i: 確定済みのバッファ先頭。ループ開始時点で pivot 未満であると判明しているところの先端を指す。
    i = begin - 1
    # j: 斥候。ループ開始時にここより前は検査済となっている。
    # begin ... end - 1 を動けば良い。(end は最初の swap の結果 pivot 自身がいるため探索しなくて良い)
    for j in range(begin, end):
        if key(L[j]) <= key(pivot):
            i += 1
            L[j], L[i] = L[i], L[j]
    L[i+1], L[end] = L[end], L[i+1]
    return i+1




def simple_quick_sort(L: List[Num], begin: int, end: int, key=lambda x: x) -> None:
    """
    nth_element 関数を用いて L[begin:end] を 破壊的に不安定でクイックソートする O(nlgn)

    Args:
        L (list)
        begin, end (int)
    
    Examples:
        >>> seq = [3, 5, 2, 1, 0, 3]
        >>> simple_quick_sort(seq, 0, 6)
        >>> seq
        [0, 1, 2, 3, 3, 5]
    """
    if end - begin > 1:
        # pivot_ind は begin ... end -1 から選ばれてほしい
        # mid = nth_element(L, random.randint(begin, end - 1), begin, end, key)
        mid = nth_element(L, end - 1, begin, end, key)
        simple_quick_sort(L, begin, mid, key)
        simple_quick_sort(L, mid+1, end, key)



def _modified_merge(left: List[Num], right: List[Num], key=lambda x: x) -> Tuple[int, List[Num]]:
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
    buf_1 = left[:] + [[None, float('inf')]]
    buf_2 = right[:] + [[None, float('inf')]]
    for _ in range(len(left) + len(right)):
        if key(buf_1[i]) <= key(buf_2[j]):
            sorted_list.append(buf_1[i])
            i += 1
        else:
            sorted_list.append(buf_2[j])
            j += 1
        inv += 1
    return inv, sorted_list


# verified @AOJ ALDS1_5_B
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B&lang=ja
def modified_merge_sort(L, begin, end, key=lambda x: x):
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
    left_inv_cnt, left = modified_merge_sort(L, begin, mid, key)
    right_inv_cnt, right = modified_merge_sort(L, mid, end, key)
    merge_inv_cnt, sorted_list = _modified_merge(left, right, key)
    return left_inv_cnt + right_inv_cnt + merge_inv_cnt, sorted_list





if __name__ == "__main__":
    n = int(input())
    L = []
    for _ in range(n):
        char, num = input().split()
        num = int(num)
        L.append([char, num])
    _, stable_seq = modified_merge_sort(L, 0, n, key=lambda x: x[1])
    simple_quick_sort(L, 0, n, lambda x: x[1])
    
    print('Stable') if stable_seq == L else print('Not stable')
    # for elm in stable_seq:
    #     print(*elm, sep=' ')
    for elm in L:
        print(*elm, sep=' ')
