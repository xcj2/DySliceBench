# [temp1.py] => [29-07-2020 @ 10:25:10] 
# Author & Template by : Udit "luctivud" Gupta
# https://www.linkedin.com/in/udit-gupta-1b7863135/


import math;   from collections import *
import sys;    from functools import reduce
import time;   from itertools import groupby

# sys.setrecursionlimit(10**6)

def input()         : return sys.stdin.readline()
def get_ints()      : return map(int, input().strip().split())
def get_list()      : return list(get_ints())
def get_string()    : return list(input().strip().split())
def printxsp(*args) : return print(*args, end="")
def printsp(*args)  : return print(*args, end=" ")


DIRECTIONS = [(+0, +1), (+0, -1), (+1, +0), (+1, -1)] 
NEIGHBOURS = [(-1, -1), (-1, +0), (-1, +1), (+0, -1),\
              (+1, +1), (+1, +0), (+1, -1), (+0, +1)]


CAPS_ALPHABETS = {chr(i+ord('A')) : i for i in range(26)}
SMOL_ALPHABETS = {chr(i+ord('a')) : i for i in range(26)}
INF = float('inf')


# Custom input output is now piped through terminal commands.
# for _test_ in range(int(input())): 

maxn = int(5e5) + 2
  
def update(idx, val, bit, n): 
    while idx <= n: 
        bit[idx] += val 
        idx += idx & -idx 
  
def query(idx, bit, n): 
    summ = 0
    while idx: 
        summ += bit[idx] 
        idx -= idx & -idx 
    return summ 
  
def solve(arr, n, queries, q): 
    bit = [0] * (n + 1) 
    prev = [-1] * maxn  
    ans = [0] * q 
    count = 0
    for i in range(n): 
        if prev[arr[i]] != -1: 
            update(prev[arr[i]] + 1, -1, bit, n) 
        prev[arr[i]] = i 
        update(i + 1, 1, bit, n) 
        while count < q and queries[count][2] == i: 
            ans[queries[count][0]] = query(queries[count][2] + 1, bit, n) - query(queries[count][1], bit, n) 
            count += 1
    for i in range(q): 
        print(ans[i]) 

# main
n, q = get_ints()
a = get_list()
queries = []
for i in range(q):
	l, r = get_ints()
	queries.append((i, l-1, r-1))
queries = sorted(queries, key = lambda x: x[2]) 
solve(a, n, queries, q) 

# print("Time Elapsed: {}".format(float(S34p-S34t)))

# Binary Indexed Tree code taken from https://www.geeksforgeeks.org/queries-number-distinct-elements-subarray/
