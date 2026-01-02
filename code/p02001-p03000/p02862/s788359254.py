#import sys

#input = sys.stdin.readline
import math
import itertools
#import bisect

def sosuhante(n):
    for k in range(2, int(math.sqrt(n))+1):
        if n% k ==0:
            return False
    return True
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
#    h,w,a,b = map(int, input().split())
    x,y = map(int,input().split())
    a=max(x,y)
    b=min(x,y)

    t=a//2
    if b<t:
       ans=0
    elif (b-t)%3==0 and a%2==0:
       aa=a//2
       bb=(b-t)//3*2
       aa-=(b-t)//3
       ans=1
       ans=cmb(aa+bb,bb)

    elif (b-t+1)%3==0 and a%2!=0:
       aa=a//2
       bb=(b-t)//3*2+1
       aa -= (b - t) // 3
       ans=1
       ans=cmb(aa+bb,bb)

    else:
        ans=0


#    print(ans)
    print(ans%(10**9+7))
if __name__ == "__main__":
    main()