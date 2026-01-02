import math
from collections import deque

# -----------------
# 素数列挙
def make_prime_list(num):
    if num < 2:
        return []

    prime_list = [i for i in range(num+1)]
    prime_list[1] = 0
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0 :
            continue
        if prime > num_sqrt:
            break

    for non_prime in range(2*prime, num, prime):
        prime_list[non_prime] = 0
    
    return [prime for prime in prime_list if prime != 0]
# -----------------

# -----------------
# 素因数分解
def prime_factorization(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list(num_sqrt)

        dict_counter = {}
        for prime in prime_list:
            while num % prime == 0:
                if prime in dict_counter:
                    dict_counter[prime] += 1
                else:
                    dict_counter[prime] = 1
                num //= prime
        
        if num != 1:
            if num in dict_counter:
                dict_counter[num] += 1
            else:
                dict_counter[num] = 1

        return dict_counter
# -----------------

# -----------------
# 約数の個数
def search_divisor_num(num):
    if num < 0:
        return None
    elif num == 1:
        return 1
    else:
        divisor_num = 1
        dict_fact = prime_factorization(num)
        for value in dict_fact.values():
            divisor_num *= (value + 1)
        return divisor_num
# -----------------

n = int(input())
res = [num for num in range(1,n+1,2) if search_divisor_num(num) == 8]
print(len(res))