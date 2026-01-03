#! /usr/bin/python3
# ABC044_B
# B - 美しい文字列 / Beautiful Strings
"""
collectionsを使わないタイプ

制約
    1≤|w|≤100
    w は英小文字 (a-z) のみからなる文字列である。
"""

import collections
test_mode = False
use_Counter = True    # collections.Counter を使うかどうか


def judge_0(l):
    """
    collections.Counter を使うタイプ
    奇数会出現する要素があると False を返し、
    全ての要素が偶数回出現すると True を返す。
    """
    broken = False
    count_l = collections.Counter(l)    # l の各要素の出現回数をカウント

    if test_mode:
        print(count_l)

    for i in count_l:
        if count_l[i] % 2 == 1:
            if test_mode:
                print('break')
            broken = True
            break

    return not broken


def judge_1(l):
    """
    collections.Counter を使わないタイプ
    奇数会出現する要素があると False を返し、
    全ての要素が偶数回出現すると True を返す。
    """
    broken = False  # break したら True になるフラグ

    for i in l:
        if test_mode:
            print('{}:'.format(i), l.count(i))
            if l.count(i) % 2 == 1:
                print('break')
        if l.count(i) % 2 == 1:
            broken = True
            break

    return not broken



def main():
    """
    main関数
    """
    w = list(str(input()))  # 文字列をリストに変換
    if use_Counter:
        beautiful = judge_0(w)
    else:
        beautiful = judge_1(w)

    if beautiful:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()
