import sys
import math
#import random
#sys.setrecursionlimit(1000000)
input = sys.stdin.readline
 
############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input()))
def inara():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
################################################################
############ ---- THE ACTUAL CODE STARTS BELOW ---- ############

n=inp()
ara=inara()

xor=0
for num in ara:
	xor^=num

xor^=ara[n-1]

ans=[0]*n
ans[n-1]=xor

for i in range(n-2,-1,-1):
	xor^=ara[i]^ara[i+1]
	ans[i]=xor

print(*ans)
