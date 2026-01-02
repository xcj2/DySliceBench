from collections import deque
from heapq import heappush,heappop
import re

def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

S = input()

def main():
    FS  = int(S[:2])
    LS = int(S[2:])
    can_yymm = True
    can_mmyy = True
    if FS < 0:
        return "NA"
    if FS == 0:
        can_mmyy = False
    if FS > 12:
        can_mmyy =False
    if LS < 0:
        return "NA"
    if LS == 0:
        can_yymm =False
    if LS > 12:
        can_yymm =False
    if can_yymm and can_mmyy:
        return "AMBIGUOUS"
    if can_yymm:
        return "YYMM"
    if can_mmyy:
        return "MMYY"
    return "NA"
print(main())
