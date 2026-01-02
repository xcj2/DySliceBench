# -*- coding: utf-8 -*-
# ALDS1_4_B_BinarySearch

import sys

def input_lines():
    return sys.stdin.readlines()

def binary_search(l, v):    
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == v:
            return mid
        elif l[mid] < v:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    lines = input_lines()
    s = sorted(set(map(int, lines[1].split())))
    t = sorted(map(int, lines[3].split()))
    
    count = 0
    for v in t:
        res = binary_search(s, v)
        if res != -1:
            count += 1
            s = s[res + 1:]
    print(count)
    
main()
