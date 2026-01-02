# -*- coding: utf-8 -*-

#整数値入力 1文字の入力
def input_one_number():
    return int(input())

#整数値龍力　複数の入力
def input_multiple_number():
    return map(int, input().split())

#整数値龍力　複数の入力(配列)
def input_multiple_number_as_list():
    return list(map(int, input().split()))

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gcd(a,b)

def calc_gcd_list(l):
    gcd = l[0]
    for i in range(1, N):
        gcd = gcd(gcd, l[i])
    return gcd

def calc_lcm_list(l):
    lcm = 1
    for i in l:
        lcm = lcm * i // gcd(lcm, i)
    return lcm


N = input_one_number()
lstA = input_multiple_number_as_list()
lcm = calc_lcm_list(lstA)
pow = 10**9 +7
print(sum(lcm//a for a in lstA)%pow)
