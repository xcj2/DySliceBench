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
    return gcd(b, a % b);x

def take_input():
	if os.environ.get("check"):
		sys.stdin = open('input.txt', 'r') 
		sys.stdout = open('output.txt', 'w')
		
take_input()
######################### TEMPLATE ENDS HERE #################################

n = int(input())
if n >= 30:
    print("Yes")
else:
    print("No")