import sys
input=sys.stdin.readline
from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())
 
def ss_raw():
    return input().split()
 
def ints_raw():
    return tuple(map(int, ss_raw()))


DIV=10**9+7

#N,A,B,C = ints_raw()
ESP_C = "$"
S=input()

def main():
    nS = S.replace("BC",ESP_C)
    ans =0
    a_buf =0
    for idx,c in enumerate(nS):
        if c == "A":
            a_buf+=1
        elif c == ESP_C:
            ans+=a_buf
        else:
            a_buf =0
    return ans

print(main())
