#coding: utf-8

from math import log10

def getLS(N):
    small = N//2
    large = N//2 + N%2
    return large, small

def getDigit(num):
    n_sum = 0
    for i in range(int(log10(num))+1):
        n_sum += num % 10
        num //= 10
    return n_sum

def getDigitSum(n1, n2):
    return getDigit(n1) + getDigit(n2)

def main(N):
    n_min = pow(10, 5)
    large, small = getLS(N)
    while small >= 1:
        tmp = getDigitSum(large, small)
        if n_min > tmp:
            n_min = tmp
        large += 1
        small -= 1
    return n_min

if __name__ == "__main__":
    N = int(input())
    print(main(N))
