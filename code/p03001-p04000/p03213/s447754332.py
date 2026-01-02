from collections import Counter,defaultdict,deque
import sys
import bisect
import math
import itertools
import string
import queue
import copy
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
 
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return [list(map(int, input().split())) for _ in range(n)]

def f(x):
    global e
    return len(list(filter(lambda y:y>=x-1,e)))

def main():
    n = inp()
    global e
    e = [0 for _ in range(n+1)]
    for i in range(2,n+1):
        x = i
        for j in range(2,i+1):
            while x % j == 0:
                e[j] += 1
                x //= j
    print( f(75) + f(25)*(f(3)-1) + f(15)*(f(5)-1) + f(5)*(f(5)-1)*(f(3)-2)//2)

if __name__ == "__main__":
    main()