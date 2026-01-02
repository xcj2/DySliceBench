import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()

G = []

def dfs(n, string, next_usable):
    if n == 0:
        G.append(string)
        return
    for char in next_usable:
        new_string = string + char
        if char == next_usable[-1]:
            added_char = chr(ord(char) + 1)
            next_usable += added_char
        dfs(n-1, new_string, next_usable)

def main():
    N = I()
    string = 'a'
    dfs(N, '', 'a')
    for string in G:
        print(string)


main()

