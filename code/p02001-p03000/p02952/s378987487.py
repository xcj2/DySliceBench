# coding: utf8

import math

def read_int():
    return int(input())

 
def read_int_n():
    return list(map(int, input().split()))
 
 
def read_str():
    return input()
 
 
def read_str_n():
    return list(map(int, input().split()))

def main():
    n = read_int()
    keta = math.floor(math.log10(n)) + 1
    ans = 0
    for i in range(1, keta):
        if i % 2 == 0:
            continue
        else:
            plus = ( 10 ** i ) - (10 ** (i-1))
            ans += plus
    if keta % 2 == 1:
        ans += n - (10 ** (keta - 1)) + 1
    print(ans)

main()