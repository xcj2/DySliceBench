from collections import defaultdict
import math
n = int(input())

def primelist(num):
    if num < 2:
        return []

    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]

def prime_factorization(num):
    if num <= 1:
        return False
    else:
        num_sqrt = math.floor(math.sqrt(num))
        prime_list = primelist(num_sqrt)

        dict_counter = defaultdict(int)
        for prime in prime_list:
            while num % prime == 0:
                dict_counter[prime] += 1
                num //= prime
        if num != 1:
            dict_counter[num] += 1

        dict_counter = dict(dict_counter)

        return dict_counter

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

cnt = 0
for i in range(1, n+1):
    if i%2 != 0:
        if search_divisor_num(i) == 8:
            cnt+=1
print(cnt)

exit(0)