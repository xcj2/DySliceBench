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
    l, r = rinput()
    q = []
    for i in range(l, r):
        for j in range(i + 1, r + 1):
            res = i * j % 2019
            q.append(res)
            if res == 0:
                print(0)
                return 0
    print(min(q))
main() 