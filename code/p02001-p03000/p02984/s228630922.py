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
    n = iinput()
    q = rlinput()
    res = [0] * n
    res[0] = sum(q) - 2 * sum(q[1::2])
    for i in range(1, n):
        res[i] = 2 * q[i - 1] - res[i - 1]
    res = map(str, res)
    print(*res)
main() 