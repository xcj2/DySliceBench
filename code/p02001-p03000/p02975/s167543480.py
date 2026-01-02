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
def _I(): return int(sys.stdin.readline())
def _F(): return float(sys.stdin.readline())
def _pf(s): return print(s, flush=True)

N = _I()
A = LI()

# 001, 101, 1000の場合など、最大桁数のものが1つしかない場合、絶対に1000と作る数は1XXXになるので、絶対無理
# 1000, 1001, 0101, 0001の場合、0001が作れる。しかし、1000はどう頑張っても作れない
# 全数字を2進数に直す結局全部1が並ぶやつ、つまり、1/1/0, 10/01/11, 111/100/011, 111/101/010などの組み合わせが必要
# そもそも3種類以上ある場合は絶対成り立たない
set_A = set(A)
if len(set_A) > 3:
    print('No')
    exit()

if len(set_A) == 1:
    if A[0] == 0:
        print('Yes')
    else:
        print('No')
elif len(set_A) == 2:
    # 2種類で成り立つのは、全部1111が2つと、全部000が1つの場合のみ
    A_list = list(set_A)
    if 0 in A_list:
        non_zero = [i for i in A_list if i != 0][0]
        if A_list[0] ^ A_list[1] == non_zero:
            # 0と1の比率が1:2でないとだめ。さらに、総数が3*2*n
            if A.count(0) * 2 == A.count(non_zero) and N % 3 == 0:
                # XORがA_listに入ってたら。
                print("Yes")
                exit()
            else:
                print('No')
                exit()
        else:
            print("No")
            exit()
    else:
        print('No')
        exit()
elif len(set_A) == 3:
    A_list = list(set_A)
    if A_list[0] ^ A_list[1] == A_list[2] and A_list[0] ^ A_list[2] == A_list[1] and A_list[1] ^ A_list[2] == A_list[0]:
        # それぞれの数が1:1:1でないとだめ
        if A.count(A_list[0]) == A.count(A_list[1]) == A.count(A_list[2]) and N % 3 == 0:
            print('Yes')
        else:
            print("No")
    else:
        print('No')


