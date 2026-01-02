import sys
from math import ceil

def input():
    return sys.stdin.readline().strip()

def iinput():
    return int(input())

def finput():
    return float(input())

def tinput():
    return input().split()

def rinput():
    return map(int, tinput())

def rlinput():
    return list(rinput())

def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)    


def main():
    n, x = rinput()
    l = rlinput()
    d = 0
    res = 1
    for i in range(n):
        d += l[i]
        if d > x:
            break
        else:
            res += 1
    print(res)
    
    
    
main()