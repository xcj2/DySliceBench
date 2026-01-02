from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial


def divisor(n): #nの約数を全て求める
    i = 1
    table = set()
    while i * i <= n:
        if n%i == 0:
            table.add(i)
            table.add(n//i)
        i += 1
    table = list(table)
    table.sort(reverse=True)
    return table


def check(data, ele, num, k):
    plus, minus = 0, 0
    amari_dic = defaultdict(int)
    for i in range(num):
        now_num = data[i]
        amari = now_num % ele
        amari_dic[amari] += 1
        # if now_num >= ele:
        #     plus += now_num - ele
        # else:
        #     minus += ele - now_num

    amari_dic = sorted(amari_dic.items(), key=lambda x: x[0])

    for amari, kosuu in amari_dic:
        if amari == 0:
            continue
        ikeru = min((k - plus) // amari, kosuu)
        plus += ikeru * amari
        minus += (kosuu - ikeru) * (ele - amari)


    # print(ele, plus, minus, amari_dic)
    if max(plus, minus) <= k:
        return 1
    else:
        return 0

def main():

    num, k = map(int, input().split())
    data = list(map(int, input().split()))

    sum_num = sum(data)
    yakusuu_list = divisor(sum_num)

    # print(yakusuu_list)

    for ele in yakusuu_list:
        if check(data, ele, num, k):
            print(ele)
            sys.exit()







if __name__ == '__main__':
    main()
