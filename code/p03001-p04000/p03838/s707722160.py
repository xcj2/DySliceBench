#!/usr/bin/env python3
import sys
import copy
# input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int,input().split())
def LI(): return list(map(int,input().split()))

def main():
    x,y = MAP()
    if 0<=x<y:
        print(y-x)
    elif x<0<y:
        if abs(x) <= y:
            print(y-abs(x)+1)
        else:
            print(abs(x)-y+1)
    elif x<y<=0:
        print(y-x)
    elif 0<y<x:
        print(x+y)
    elif y<=0<x:
        if abs(y)<=x:
            print(x-abs(y)+1)
        else:
            print(abs(y)-x+1)
    elif y<x<0:
        print(x-y+2)
    elif y<x<=0:
        print(x-y+1)

    return

if __name__ == '__main__':
    main()
