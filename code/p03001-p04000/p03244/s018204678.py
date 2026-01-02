import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    v = LI()

    vset = set(v)
    if len(vset) == 1:
        print(len(v)//2)
        exit()

    #  n = 10**5
    #  #  v = [10**5 - i%18 for i in range(n)]
    #  v = [random.randint(0, 100) for i in range(n)]
    #  print(v[:10])

    odd = []
    even = []
    for idx, i in enumerate(v):
        if idx % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    # Counterが速い
    odd_count = collections.Counter(odd)
    even_count = collections.Counter(even)

    #  print(odd_count, even_count)
    if len(odd_count) == len(even_count) == 1:
        # 変更の必要なし
        print(0)
        exit()

    if odd_count.most_common(1)[0][0] != even_count.most_common(1)[0][0]:
        # 楽なほう
        if len(odd_count) == 1:
            even_result = sum([i[1] for i in even_count.most_common()[1:]])
            print(even_result)
        elif len(even_count) == 1:
            odd_result = sum([i[1] for i in odd_count.most_common()[1:]])
            print(odd_result)
        else:
            odd_result = sum([i[1] for i in odd_count.most_common()[1:]])
            even_result = sum([i[1] for i in even_count.most_common()[1:]])
            print(odd_result + even_result)
    else:
        # 全部同じ数字にならないようにしたい
        # ２個め同士で比べて、２個めをより多く含んでる方はそっちにしちゃう
        if len(odd_count) == 1:
            even_result = even_count.most_common(1)[0][1]
            even_result += sum([i[1] for i in even_count.most_common()[2:]])
            print(even_result)
        elif len(even_count) == 1:
            odd_result = odd_count.most_common(1)[0][1]
            odd_result += sum([i[1] for i in odd_count.most_common()[2:]])
            print(odd_result)
        elif odd_count.most_common(2)[1][1] > even_count.most_common(2)[1][1]:
            # oddは２つめに多いものを不変にする
            # evenは１つめを不変に
            odd_result = odd_count.most_common(1)[0][1]
            odd_result += sum([i[1] for i in odd_count.most_common()[2:]])
            even_result = sum([i[1] for i in even_count.most_common()[1:]])
            print(odd_result + even_result)
        else:
            odd_result = sum([i[1] for i in odd_count.most_common(len(odd_count))[1:]])
            even_result = even_count.most_common(1)[0][1]
            even_result += sum([i[1] for i in even_count.most_common()[2:]])
            print(odd_result + even_result)

main()
