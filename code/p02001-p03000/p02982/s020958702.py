import sys
from math import ceil
from operator import itemgetter as get

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

def nod(a, b):
    while b: 
        a, b = b, a % b
    return a
 
def calc(n, c, d):
    return n - n // c - n // d + n // (c * d // nod(c, d))   


def main():
    res, x = 0, []
    n, d = rinput()
    for i in range(n):
        x.append(rlinput())
     
    for o in range(n - 1):
        for u in range(o + 1, n):
            if ((sum((i - j) ** 2 for i, j in zip(x[o], x[u]))) ** 0.5).is_integer():
                res += 1
    print(res)
main() 