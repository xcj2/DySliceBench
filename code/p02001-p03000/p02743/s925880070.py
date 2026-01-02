import sys
input = sys.stdin.readline
# import math
# sqrt = math.sqrt

# def int_sqrt2(n):
#     def f(prev):
#         while True:
#             m = (prev + n / prev) / 2
#             if m >= prev:
#                 return prev
#             prev = m
    
#     return f(int(sqrt(n) * (1 + 1e-20)))

# from decimal import *

# getcontext().prec = 20      # デフォルト28桁のところを20桁にする
# m = int(Decimal(n).sqrt())
# print m ** 2 - n            # -2222221948

def linput():
    return list(map(int, input().split()))

def gcd(n,m):
    while m:
        n,m = m, n%m
    return n

def lcm(n,m):
    return n*m//gcd(n,m)


def main():
    # N = int(input())
    A,B,C = linput()
    # vA = linput()
    # S = input()
    # mX = [linput() for _ in [0,]*N]

    # res = 0
    # res = -(-N//M)

    # LH = A**.5 + B**.5
    # RH = C**.5

    # rtAB = int(Decimal(A*B).sqrt())
    # rtAB = int_sqrt2(A*B)

    LH = A * B * 4
    RH = (C-A-B)**2

    # LH = A * B * 4
    # RH = abs(C-A-B)
    print(LH,RH, file=sys.stderr)

    res = ("No","Yes")[LH < RH if C-A-B>=0 else 0]

    print(res)

main()
