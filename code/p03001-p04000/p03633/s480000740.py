import sys
from collections import defaultdict, deque
from functools import reduce
import math

input = sys.stdin.readline

def chmax(a, b):
    if a > b:
        return a
    else:
        return b
    
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def main():
    N = int(input())
    T = [int(input()) for _ in range(N)]
    print(lcm(*T))


if __name__ == '__main__':
    main()
