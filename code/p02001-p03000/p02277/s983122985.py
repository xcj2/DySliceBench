# -*- coding: utf-8 -*-
"""
Created on Thu May  3 21:24:25 2018
ALDS1_6_C
@author: maezawa
"""
a = []
n = int(input())
for i in range(n):
    s = input().split()
    a.append([s[0], int(s[1])])
    
a_in = a.copy()

def is_stable(a, b):
    s = True
    for i in range(n-1):
        if b[i+1][1] == b[i][1]:
            j = a.index(b[i])
            k = a.index(b[i+1])
            if j > k:
                s = False
                return s
    return s
    

def partition(a, p, r):
    x = a[r][1]
    i = p - 1
    for j in range(p, r):
        if a[j][1] <= x:
            i += 1
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    temp = a[i+1]
    a[i+1] = a[r]
    a[r] = temp
    return i+1
    
def quick_sort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quick_sort(a, p, q-1)
        quick_sort(a, q+1, r)

quick_sort(a, 0, len(a)-1)
if is_stable(a_in, a):
    print('Stable')
else:
    print('Not stable')
for i in range(len(a)):
    print('{} {}'.format(a[i][0],a[i][1]))


