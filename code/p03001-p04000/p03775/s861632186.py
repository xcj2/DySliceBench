import math
import operator
from itertools import *
from functools import *


def main():
    #infile = open("compprog.txt", mode="r")
    n = int(input())
    res = -1
    divisors_found = set()
    for subset in powerset(prime_factors(n)):
        div1 = prod(subset)
        if div1 not in divisors_found:
            div2 = n // div1
            this_f = f(div1, div2)
            if res == -1 or this_f < res:
                res = this_f
            divisors_found.add(div1)
            divisors_found.add(div2)
    print(res)
    #infile.close()


def f(a, b):
    return max(len(str(a)), len(str(b)))


def prime_factors(num):
    factor_list = []
    while num % 2 == 0:
        factor_list.append(2)
        num //= 2
    i = 3
    while i <= math.sqrt(num):
        if num % i == 0:
            factor_list.append(i)
            num //= i
            i = 3
        else:
            i += 2
    if num > 1:
        factor_list.append(num)
    return factor_list


def powerset(iterable):
    s = list(iterable)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))


def prod(iterable):
    return reduce(operator.mul, iterable, 1)



if __name__ == "__main__":
    main()
