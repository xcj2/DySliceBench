import math
from itertools import product
class Eratos:
    def __init__(self, num):
        assert(num >= 1)
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
        """
        >>> e = Eratos(100)
        >>> [i for i in range(1, 101) if e.is_prime(i)]
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        """
        assert(num >= 1)
        if num > self.table_max:
            raise ValueError('Eratos.is_prime(): exceed table_max({}). got {}'.format(self.table_max, num))
        return self.table[num]
    
    def prime_factorize(self, num):
        """
        >>> e = Eratos(10000)
        >>> e.prime_factorize(6552)
        {2: 3, 3: 2, 7: 1, 13: 1}
        """
        assert(num >= 1)
        if int(math.sqrt(num)) > self.table_max:
            raise ValueError('Eratos.prime_factorize(): exceed prime table size. got {}'.format(num))
        factorized_dict = dict()    # 素因数分解の結果を記録する辞書
        candidate_prime_numbers = [i for i in range(2, int(math.sqrt(num)) + 1) if self.is_prime(i)]
        # n について、√n 以下の素数で割り続けると最後には 1 or 素数となる
        # 背理法を考えれば自明 (残された数が √n より上の素数の積であると仮定。これは自明に n を超えるため矛盾)
        for p in candidate_prime_numbers:
            # これ以上調査は無意味
            if num == 1:
                break
            if num % p == 0:
                cnt = 0
                while num % p == 0:
                    num //= p
                    cnt += 1
                factorized_dict[p] = cnt
        if num != 1:
            factorized_dict[num] = 1
        return factorized_dict
    
    def enum_divisor(self, num):
        """
        >>> e = Eratos(10000)
        >>> e.enum_divisor(4)
        [1, 2, 4]
        >>> e.enum_divisor(19)
        [1, 19]
        >>> e.enum_divisor(100)
        [1, 5, 25, 2, 10, 50, 4, 20, 100]
        """
        factorized_dict = self.prime_factorize(num)
        primes = list(factorized_dict.keys())
        all_pattern_powers = product(*[range(i + 1) for i in factorized_dict.values()])    # 各素数を 0 to value 個まで任意回かけるとする。その全パターンを列挙
        divisor = []
        for power_pattern in all_pattern_powers:
            tmp = 1
            for i in range(len(power_pattern)):
                tmp *= pow(primes[i], power_pattern[i])
            divisor.append(tmp)
        return divisor

N, M = map(int, input().split())
eratos = Eratos(int(math.sqrt(M)) + 1)
L = eratos.enum_divisor(M)
L.sort(reverse=True)
for div in L:
    if div * N <= M:
        print(div)
        exit()