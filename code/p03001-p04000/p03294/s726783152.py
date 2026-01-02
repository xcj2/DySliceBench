# coding: utf-8

def gcd(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1

    while n1 % n2 != 0:
        rest = n1 % n2
        n1, n2 = n2, rest

    return n2

def lcm(n1, n2):
    return n1 * n2 // gcd(n1, n2)

def getM(alist):
    nLcm = lcm(alist[0], alist[1])
    for i in range(2, len(alist)):
        nLcm = lcm(nLcm, alist[i])
    
    return nLcm-1

def f(m, alist):
    t_sum = 0
    for ai in alist:
        t_sum +=  m % ai

    return t_sum
    
if __name__ == "__main__":
    N = int(input())
    alist = [int(x) for x in input().split(" ")]
    print(f(getM(alist), alist))
    
