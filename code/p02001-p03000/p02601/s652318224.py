import sys
import os
# import math
# input = sys.stdin.readline

def int_array():
    return list(map(int, input().strip().split()))


def str_array():
    return input().strip().split()

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b);

def take_input():
	if os.environ.get("check"):
		sys.stdin = open('input.txt', 'r') 
		sys.stdout = open('output.txt', 'w')
		
take_input()
######################### TEMPLATE ENDS HERE #################################

a,b,c = int_array()
k = int(input())

# conditions
#c>b>a

count = 0

for _ in range(k):
    if a>=b:
        b*=2
    elif b>=c:
        c*=2
    if a<b<c:
        break

if a<b<c:
    print("Yes")
else:
    print("No")