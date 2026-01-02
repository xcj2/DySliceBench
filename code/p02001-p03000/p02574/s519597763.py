import sys
import bisect
import itertools
import collections
import fractions
import heapq
import math
from operator import mul
from functools import reduce
from functools import lru_cache


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))



    def get_primenumber(number):  # エラトステネスの篩
        prime_list = []
        search_list = list(range(2, number + 1))
        # search_listの先頭の値が√nの値を超えたら終了
        while search_list[0] <= math.sqrt(number):
            # search_listの先頭の値が√nの値を超えたら終了
            # search_listの先頭をprime_listに入れて、先頭をリストに追加して削除
            head_num = search_list.pop(0)
            prime_list.append(head_num)
            # head_numの倍数を除去
            search_list = [num for num in search_list if num % head_num != 0]
        # prime_listにsearch_listを結合
        prime_list.extend(search_list)
        return prime_list


    def prime_factor_table(n):
        table = [0] * (n + 1)
        for i in range(2, n + 1):
            if table[i] == 0:
                for j in range(i + i, n + 1, i):
                    table[j] = i
        return table

    def prime_factor(n, prime_factor_table):
        prime_count = collections.Counter()

        while prime_factor_table[n] != 0:
            prime_count[prime_factor_table[n]] += 1
            n //= prime_factor_table[n]
        prime_count[n] += 1

        return prime_count

    table = prime_factor_table(10**6+10)

    numset = set()
    for i in A:
        thedic = prime_factor(i, table)
        for l in thedic.keys():
            flag = True
            if l in numset and l != 1:
                flag = False
                break
        if flag:
            tmpset = set(thedic.keys())
            numset |= tmpset
        else:
            break
    if flag:
        print('pairwise coprime')
        sys.exit()
    else:
        flag = True
        theset = set(prime_factor(A[0], table).keys())
        for i in A[1:]:
            thedic = prime_factor(i, table)
            theset = theset & set(thedic.keys())
            if len(theset) == 0:
                print('setwise coprime')
                flag = False
                break
    if flag:
        print('not coprime')



if __name__ == '__main__':
    solve()