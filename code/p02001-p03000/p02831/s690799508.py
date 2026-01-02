from sys import stdin
import sys
import math
import numpy as np
##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    A, B = rip()
    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)
    g = gcd(A, B)
    print(A // g * B)


if __name__ == "__main__":
    main()
