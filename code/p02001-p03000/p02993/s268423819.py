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
    a = list(input())
    if a[0] == a[1] or a[1] == a[2] or a[3] == a[2]:
        print("Bad")
        return 0
    print("Good")
    
    
    
    
main() 