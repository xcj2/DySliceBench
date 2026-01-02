
import sys
import math
import bisect
import copy
sys.setrecursionlimit(1000000)
from collections import deque

def bubble(a,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if a[j][1]<a[j-1][1]:
                a[j],a[j-1] = a[j-1],a[j]

def selection(a,n):
    for i in range(n):
        minj = i
        for j in range(i+1,n):
            if a[j][1]<a[minj][1]:
                minj = j
        a[i],a[minj] = a[minj],a[i]

def main():
    n = int(input())
    a = list(input().split())
    b = copy.copy(a)
    bubble(a,n)
    selection(b,n)
    print (' '.join(a))
    print ('Stable')
    print (' '.join(b))
    if a==b:print ('Stable')
    else   :print ('Not stable')



if __name__ == '__main__':
    main()


