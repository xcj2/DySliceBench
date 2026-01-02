# -*- coding: utf-8 -*-

#整数値入力 1文字の入力
def input_one_number():
    return int(input())

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

#整数値龍力　複数の入力(配列)
def input_multiple_number_as_list():
    return list(map(int, input().split()))

#整数値龍力　複数の入力(配列で1つずつ渡される)
def input_multiple_number_as_list_sep(N):
    ins = []
    for i in range(N):
        ins.append(input())
    return ins

#2次元配列入力
def input_map():
    return [list(map(int,list(input()))) for i in range(h)]

#リスト出力
def print_list(list):
    print(*list)
    return

#2次元配列出力
def print_map(maplist):
    for i in maplist:print(*i, sep='')
    return

#素数生成
def generate_primenums():
    n = 100
    primes = set(range(2, n+1))
    for i in range(2, int(n**0.5+1)):
        primes.difference_update(range(i*2, n+1, i))
    primes=list(primes)
    return primes

def memo():
    a=[0]*5
    b=a  #良くない配列のコピー
    b2=a[:]  #1次元のときはコピーはこれで良い
    a[1]=3
    print('b:{}, b2:{}'.format(b,b2))  #b:[0, 3, 0, 0, 0], b2:[0, 0, 0, 0, 0]
    
    import copy
    a= [[0]*3 for i in range(5)] #2次元配列はこう準備、[[0]*3]*5だとだめ
    b=copy.deepcopy(a)  #2次元配列はこうコピーする
    
    #内包表記奇数のみ
    odd=[i for i in range(100) if i%2==1] #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    #二部探索
    import bisect
    a = [1, 2, 3, 5, 6, 7, 8, 9]
    b=bisect.bisect_left(a, 8)

    #combinations、組み合わせ、順列
    from itertools import permutations, combinations,combinations_with_replacement,product
    a=['a','b','C']
    print(list(permutations(a)))
    print(list(combinations(a,2)))
    print(list(combinations_with_replacement(a,3)))


#階乗
def kaijo(n):
    import math
    return math.factorial(n)

#選び方（コンビネーション nCr）
def num_combination(n,r):
    import math
    return math.factorial(n) // math.factorial(n - r)


#最大公約数、最小公倍数
def calc_gcd(a,b):
    import fractions
    GCD=fractions.gcd(a,b)
    lcm=a*b//gcd
    return gcd,lcm

#複数の最大公約数
def calc_gcd_list(l):
    gcd = l[0]
    for i in range(1, N):
        gcd = fractions.gcd(gcd, l[i])
    return gcd

#各桁の和
def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n%10
        n //= 10
    return sum

N = input_one_number()
lst_d = input_multiple_number_as_list_sep(N)

lst_d.sort()

dan = len(lst_d)

before = 100000
for i in lst_d:
    if before == i:
        dan -= 1
    before = i

print(dan)
