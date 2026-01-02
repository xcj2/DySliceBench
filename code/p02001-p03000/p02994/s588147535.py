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
    n, l = rinput()
    a = []
    for i in range(n):
        a.append(l + i)
    w = sum(a)
    if a[0] >= 0:
        print(w - a[0])
    elif a[-1] <= 0:
        print(w - a[-1])
    else:
        print(w)
            
        
    
    
    
    
main() 