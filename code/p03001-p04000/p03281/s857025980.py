import math
 
def make_prime_list_2(num):
    if num < 2:
        return []
 
    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)
 
    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break
 
        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0
 
    return [prime for prime in prime_list if prime != 0]
 
def prime_factorization_2(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = make_prime_list_2(num_sqrt)
 
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
 
def search_divisor_num_2(num):
    if num < 0:
        return None
    elif num == 1:
        return 1
    else:
        divisor_num = 1
        dict_fact = prime_factorization_2(num)
        for value in dict_fact.values():
            divisor_num *= (value + 1)
        return divisor_num
 
eight_list = []
for i in range(100):
    ii = i * 2 + 1
    if search_divisor_num_2(ii) == 8:
        eight_list.append(ii)
 
n = int(input())
use_list = [1 for i in eight_list if i <= n]
print(sum(use_list))