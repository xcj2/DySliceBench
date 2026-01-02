from heapq import heappush,heappop
import re

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))
INF = 1 << 29


def runLength(in_str):
    kukan = 1
    start = 0
    ret = []
    for i in range(1,len(in_str)):
        if in_str[i-1]!=in_str[i]:
            ret.append([in_str[i-1],kukan,start])
            start = i
            kukan=0
        kukan+=1
    ret.append([in_str[-1],kukan,start])
    return ret

N = int_raw()
S= input()
K = int_raw()
dp = {}

def rec(ss):
    return 0

def main():
    return re.sub("[^"+S[K-1]+"]","*",S)



print(main())

