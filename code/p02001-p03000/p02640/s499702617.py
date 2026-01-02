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

x,y=invr()

for i in range(x+1):
	a=i*2
	b=(x-i)*4
	
	if a+b==y:
		print("Yes")
		exit(0)

print("No")


	
