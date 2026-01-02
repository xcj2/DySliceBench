import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def count_bit_one(bits, n):
    ret = 0
    for keta in range(n):
        if bits & 2**keta:
            ret += 1
    return ret

def is_honest(bits, i):
    return bits & 2**i != 0

n = int(input())
aaa = [None] * n
for i in range(n):
    a = int(input())
    aaa[i] = [ get_nums_l() for _ in range(a)]

# log(aaa)

ans = -1
# 0:不親切 1:正直
for bits in range(2**n):
    ng = False
    for keta in range(n):
        if is_honest(bits, keta):
            for a in aaa[keta]:
                if is_honest(bits, a[0]-1) != (a[1]==1):
                    ng = True
                    break
        if ng:
            break
    if not ng:
        # log("OK:", bits)
        ans = max(ans, count_bit_one(bits, n))

print(ans)