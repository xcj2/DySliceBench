import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)
from fractions import Fraction

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def inv(x, MOD):
    return pow(x, MOD-2, MOD)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n,k,*A = get_all_int()
    A = list(A)

    # 答えが負である条件
    # ・Aが全て負で、Kが奇数
    # ・Aの負数が奇数個かつ0が存在せず、K=N

    # 答えが0である条件
    # ・N-(Aの0の個数) < K

    positives = 0
    zeros = 0
    negatives = 0

    for a in A:
        if a > 0:
            positives += 1
        elif a == 0:
            zeros += 1
        else:
            negatives += 1
    

    if k == 1:
        # 1個だけの場合はたんに最大値を出力する
        A.sort(reverse=True)
        print(A[0])
        exit()

    if (n-zeros) < k:
        # 答えが0
        print(0)
        exit()
    
    elif (k==n and negatives%2==1  or  n==negatives+zeros and k%2==1):
        # 答えが負
        # 絶対値小さい順にK個掛ける
        A.sort(key=lambda a: abs(a))
        # log(A)
        ans = 1
        for i in range(k):
            ans =  (ans * A[i]) % MOD
        print(ans%MOD)
        exit()

    else:
        # 答えが正
        # 絶対値大きい順にK個掛ける
        A.sort(reverse=True, key=lambda a: abs(a))
        # log(A)
        ans = 1
        n_count = 0
        last_n = 0
        last_p = 0
        for i in range(k):
            a = A[i]
            ans =  (ans * a) % MOD
            if a < 0:
                n_count += 1
                last_n = a
            elif a > 0:
                last_p = a
                # log(i, last_n)

        # log(ans, n_count, last_n)
        
        # 負数を奇数個選んでいる場合は調整する
        if n_count%2 == 1:
            first_p = None
            first_n = None
            for i in range(k,n):
                a = A[i]
                if a > 0 :
                    ans_a = ans*inv(last_n, MOD) * a
                    first_p = a
                    break
            if last_p != 0:
                for i in range(k,n):
                    a = A[i]
                    if a < 0:
                        ans_b = ans*inv(last_p, MOD) * a
                        first_n = a
                        break
                if first_n is not None:
                    if first_p is not None:
                        xx = Fraction(abs(first_p), abs(last_n))
                        yy = Fraction(abs(first_n), abs(last_p))
                        # xx = abs(first_p) / abs(last_n)
                        # yy = abs(first_n) / abs(last_p)
                        if yy > xx:
                            ans_a = ans_b
                    else:
                        ans_a = ans_b
            if first_n is None and first_p is None:
                ans_a = 0
            ans = ans_a
        
        print(ans%MOD)
        exit()

main()