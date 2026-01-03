import collections
import itertools
import numpy as np
import sys
MAX_INT = int(10e10)
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def combi(a,b):
	num = 1
	for j in range(b):
		num = num*(a-j)//(j+1)
	return num

N,P = IL()
A = IL()

odd = 0
even = 0
for i in A:
	if i%2 != 0:
		odd += 1
	else:
		even += 1

zero = 1
if even != 0:
	for i in range(1,even+1):
		zero += combi(even,i)

if P == 1:
	ans = 0
	for i in range(1,odd+1,2):
		ans += combi(odd,i)*zero
else:
	ans = 0
	for i in range(0,odd+1,2):
		ans += combi(odd,i)*zero

print(ans)