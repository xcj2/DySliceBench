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

def nok(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)    


def main():
    n = iinput()
    q, res = [], 0
    for i in range(n):
        q.append(tuple(rinput()))
    q = sorted(q, key = get(1))
    for i, v in q:
        res += i
        if res > v:
            print("No")
            return 0
    print("Yes")
main() 