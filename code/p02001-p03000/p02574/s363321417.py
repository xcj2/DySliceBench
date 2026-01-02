#!/usr/bin/env python3
import sys
from math import gcd
from functools import reduce
def input(): return sys.stdin.readline().rstrip()

def pairwaise(bools):
    for i in range(2,10**6):
        hantei=0
        for j in range(i,10**6+1,i):
            hantei+=bools[j]
        if hantei>1:
            return False
    return True


def main():
    n=int(input())
    A=list(map(int, input().split()))
    gcds=reduce(gcd,A)
    if gcds>1:
        print('not coprime')
    else:
        bools=[0]*(10**6+5)
        for AA in A:
            if bools[AA]==1 and AA!=1:
                print('setwise coprime')
                exit()
            bools[AA]+=1
        if pairwaise(bools):
            print('pairwise coprime')
        else:
            print('setwise coprime')

    
    


if __name__ == '__main__':
    main()