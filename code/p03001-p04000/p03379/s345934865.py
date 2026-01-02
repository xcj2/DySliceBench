import math
import copy
#import sys
#import bisect
#input = sys.stdin.readline
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
def lcm(a, b):
    return((a*b)//gcd(a,b))

def main():
    #x,y = map(int,input().split())	x=1,y=2
    #a = input().split()	a=['1','2','3',...,'n']
    #a = list(map(int,input().split()))	a=[1,2,3,4,5,...,n]
    #li = input().split('T')	FFFTFTTFF => li=['FFF', 'F', '', 'FF']
    n=int(input())
    a = list(map(int,input().split()))
    b=copy.copy(a)
    a.sort()
    for i in range(n):
        x=b[i]
        if x<=a[(n//2)-1]:
            print(a[(n//2)])
        else:
            print(a[(n//2)-1])

main()