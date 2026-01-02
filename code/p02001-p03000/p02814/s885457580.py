from collections import Counter, defaultdict
import sys

sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools

import queue
from collections import deque

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count2(a):
    count = 0
    while 1:
        if a % 2 == 0:
            count += 1
            a //= 2
        else:
            break
    return count

def main():
    num, m = map(int, input().split())
    data = list(map(int, input().split()))

    min_koubaisuu = data[0]

    for i in range(1, num):
        min_koubaisuu = lcm(min_koubaisuu, data[i])

    baisuu = min_koubaisuu // 2

    ans = ((m // baisuu) + 1) // 2

    count2_num = count2(data[0])
    for i in range(1, num):
        if count2_num != count2(data[i]):
            print(0)
            sys.exit()

    print(ans)




if __name__ == '__main__':
    main()
