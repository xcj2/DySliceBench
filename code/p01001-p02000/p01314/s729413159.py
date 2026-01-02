import math


def get_one_int()->int:
    one_int = int(input())
    return one_int

def make_divisors(num:int)->set:
    divisors = set()
    for i in range(1, math.floor(num ** 0.5) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return divisors

def count_odd_num(num_set)->int:
    odd_num = 0
    for i in num_set:
        if i % 2 != 0:
            odd_num += 1
    return odd_num

if __name__ == "__main__":
    while True:
        given_num = get_one_int()
        if given_num == 0:
            break
        divisors = make_divisors(given_num)
        odd_num = count_odd_num(divisors)
        odd_num -= 1 # remove 1
        print(odd_num)

