# coding: utf8

import math

const = 10 ** 9 + 7

def read_int_n():
    return list(map(int, input().split()))

def comb(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m)) 

def power(x, y):
    """
        ２分累乗法
    """
    if      y == 0      :   return 1
    elif    y == 1      :   return x % const
    elif    y % 2 == 0  :   return power(x, y/2) ** 2 % const
    else                :   return power(x, math.floor(y/2)) ** 2 * x % const

if __name__ == "__main__":
    n, m = read_int_n()
    # mを素因数分解する
    cnts = {}
    for i in range(2, math.ceil(math.sqrt(m)) + 1):
        while m % i == 0:
            if i not in cnts:
                cnts[i] = 1
            else:
                cnts[i] += 1
            m //= i
    else:
        if m > 1:
            if m not in cnts:
                cnts[m] = 1
            else:
                cnts[m] += 1
    ans = 1
    for key, value in cnts.items():
        num = 1
        for i in range(value):
            num *= (n + value - 1 - i)
        num //= math.factorial(value)
        # ans *= comb(value + n - 1, value) % const
        ans *= num % const
        ans = ans % const
    print(ans)