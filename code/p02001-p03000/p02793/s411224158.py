#!/usr/bin/env python3

import sys
import math
from collections import defaultdict


def main():
    mod = 1000000007                  # 10^9+7
    sys.setrecursionlimit(10**6)    # 1000 -> 1000000
    def input(): return sys.stdin.readline().rstrip()
    def ii():  return int(input())
    def lmi(): return list(map(int, input().split()))

    class Eratos:
        def __init__(self, num):
            self.table_max = num
            # self.table[i] は i が素数かどうかを示す (bool)
            self.table = [False if i == 0 or i == 1 else True for i in range(num+1)]
            for i in range(2, int(math.sqrt(num)) + 1):
                if self.table[i]:
                    for j in range(i ** 2, num + 1, i):    # i**2 からスタートすることで定数倍高速化できる
                        self.table[j] = False
            # self.table_max 以下の素数を列挙したリスト
            self.prime_numbers = [2] if self.table_max >= 2 else []
            for i in range(3, self.table_max + 1, 2):
                if self.table[i]:
                    self.prime_numbers.append(i)
        
        def is_prime(self, num):
            if num > self.table_max:
                raise ValueError('Eratos.is_prime(): exceed table_max({}). got {}'.format(self.table_max, num))
            return self.table[num]
        
        def prime_factorize(self, num):
            if num > self.table_max:
                raise ValueError('Eratos.prime_factorize(): exceed table_max({}). got {}'.format(self.table_max, num))
            factorized_dict = defaultdict(int)    # 素因数分解の結果を記録する辞書
            candidate_prime_numbers = [i for i in range(2, int(math.sqrt(num)) + 1) if self.is_prime(i)]
            # n について、√n 以下の素数で割り続けると最後には 1 or 素数となる
            # 背理法を考えれば自明 (残された数が √n より上の素数の積であると仮定。これは自明に n を超えるため矛盾)
            for p in candidate_prime_numbers:
                # これ以上調査は無意味
                if num == 1:
                    break
                while num % p == 0:
                    num //= p
                    factorized_dict[p] += 1
            if num != 1:
                factorized_dict[num] = 1
            return factorized_dict

    # import time
    # s = time.time()

    n = ii()
    L = lmi()
    a_max = max(L)
    # O(AlglgA) で前処理
    eratos = Eratos(a_max)
    # print('preprocessed (Eratostenes)')
    # print(time.time() - s)

    # O(n) * O(√A) で LCM を素因数分解した形で保存する
    lcm_dict = eratos.prime_factorize(L[0])
    for i in range(1, n):
        d = eratos.prime_factorize(L[i])
        for k, v in d.items():
            lcm_dict[k] = max(lcm_dict[k], v)
    # print('prime factorized')
    # print(time.time() - s)
    
    # O(√A)
    lcm_mod = 1
    for k, v in lcm_dict.items():
        lcm_mod = (lcm_mod * pow(k, v, mod)) % mod
    
    # O(n)
    ans = 0
    for a in L:
        # a^p-2 ≡ 1/a
        inverse_element = pow(a, mod-2, mod)
        ans = (ans + lcm_mod * inverse_element) % mod
    
    print(ans)
    # print(time.time() - s)

    

if __name__ == "__main__":
    main()