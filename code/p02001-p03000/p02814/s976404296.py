import sys
# import fractions
import math
from functools import reduce
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
stdin = sys.stdin

def gcd(a,b):
  while b:a,b=b,a%b
  return a

def lcm(x, y):
    return (x * y) // gcd(x, y)

def lcm_list(l):
    return reduce(lcm, l, 1)

i_i = lambda: int(i_s())
i_l = lambda: list(map(int, stdin.readline().split()))
i_s = lambda: stdin.readline().rstrip()

N, M = i_l()
a = i_l()
half_lcm = lcm_list(a) // 2

for i in a:
    if half_lcm // (i // 2) % 2 == 0:
        print(0)
        exit()

print(((M // half_lcm) + 1) // 2)