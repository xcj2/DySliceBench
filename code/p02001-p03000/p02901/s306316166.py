from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
from copy import deepcopy, copy

import queue
from collections import deque



def divisor(n): #nの約数を全て求める
    i = 1
    table = set()
    while i * i <= n:
        if n%i == 0:
            table.add(i)
            table.add(n//i)
        i += 1
    return table

ans = 10 ** 10

def check(box_num, kagi_num, kagi_data, ind, now_data_kari, money, data):
    now_data = copy(now_data_kari)

    if ind == box_num:
        for i in range(box_num):
            if now_data[i] == 0:
                break
        else:
            global ans
            ans = min(ans, money)
        return


    if now_data[ind]:
        check(box_num, kagi_num, kagi_data, ind + 1, now_data, money, data)
        return

    check_set = set()
    for i in range(len(kagi_data[ind + 1])):
        aaa = kagi_data[ind + 1][i]
        now_data = copy(now_data_kari)

        bbb = ['0' for i in range(box_num)]
        flg = 1
        for ele in data[aaa][2]:
            if now_data[ele - 1] == 0:
                now_data[ele - 1] = 1
                flg = 0
            if ele >= ind + 1:
                bbb[ele - 1] = '1'
        if flg:
            continue
        bbb = ''.join(bbb)
        if bbb in check_set:
            continue
        check_set.add(bbb)
        check(box_num, kagi_num, kagi_data, ind + 1, now_data, money + data[aaa][0], data)



def main():
    box_num, kagi_num = map(int, input().split())

    data = [0 for i in range(kagi_num)]
    kari = set()

    for i in range(kagi_num):
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        kari |= set(b)
        data[i] = [a[0], a[1], b]


    kagi_data = defaultdict(int)
    for i in range(kagi_num):
        a = data[i]
        aaa = 0
        for ele in a[2]:
            aaa += 2 ** (ele - 1)
        bin_data = bin(aaa)[2:]
        bin_data = bin_data.zfill(box_num)

        if bin_data in kagi_data:
            kagi_data[bin_data] = min(a[0], kagi_data[bin_data])
        else:
            kagi_data[bin_data] = a[0]

        aaaaaa = kagi_data.items()

        for key, value in list(aaaaaa):
            aaa = ['0' for i in range(box_num)]
            for i in range(box_num):
                if key[i] == '1' or bin_data[i] == '1':
                    aaa[i] = '1'
            aaa = ''.join(aaa)
            if aaa in kagi_data:
                kagi_data[aaa] = min(value + a[0], kagi_data[aaa])
            else:
                kagi_data[aaa] = value + a[0]


    # print(kagi_data)
    aaa = ['1' for i in range(box_num)]
    aaa = ''.join(aaa)
    if aaa in kagi_data:
        print(kagi_data[aaa])
    else:
        print(-1)



# def test():
#     for i in :
#         print(i)

if __name__ == '__main__':
    main()
    # test()
