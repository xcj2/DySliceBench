# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import bisect
import math
from operator import itemgetter

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b / gcd(a, b)

class slist(list):
    def __init__(self, *args, **kw):
        list.__init__(self, *args, **kw)
        self.sort()

    def append(self, value):
        bisect.insort(self,value)

    def index_left(self, value):
        return bisect.bisect_left(self, value)


if __name__ == '__main__':
    N = int(input())
    arr = [None] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    a = sorted(arr, key=lambda x: (x[1], x[0],))
    # print(a)
    sum = 0
    for b in a:
        sum += b[0]
        if sum > b[1]:
            print('No')
            exit()
    print('Yes')
