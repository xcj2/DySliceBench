from math import gcd
from functools import reduce

def gcd_mul(numbers):
    return reduce(gcd, numbers)

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_mul(numbers):
    return reduce(lcm, numbers)

def solve():
    from sys import stdin
    file_input = stdin
    
    from operator import mul
    
    while True:
        n = int(file_input.readline())
        if n == 0:
            break
        d_list = []
        v_list = []
        for i in range(n):
            d, v = map(int, file_input.readline().split())
            d_list.append(d)
            v_list.append(v)
        
        mv = reduce(mul, v_list)
        x = [mv * d // v for d, v in zip(d_list, v_list)]
        l = lcm_mul(x)
        
        for s in x:
            print(l // s)

solve()
