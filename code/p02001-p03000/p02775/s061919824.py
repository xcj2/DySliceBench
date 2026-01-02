#!/usr/bin/env python3
import sys


def solve(N):
    l=len(N)
    sw=0
    a=[0]*l
    for i in range(l):
        a[i]=int(N[i])
    a.insert(0,0)

    carry=0
    for i in reversed(range(l+1)):
        if a[i]<5:
            sw+=a[i] 
        elif a[i]==5 and a[i-1]<5:
            sw+=a[i] 
        else:
            sw+=10-a[i]
            tsugi=i-1
            while a[tsugi]==9:
                a[tsugi]=0
                tsugi-=1
            a[tsugi]+=1
    print(sw)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = next(tokens)
    solve(N)

if __name__ == '__main__':
    main()
