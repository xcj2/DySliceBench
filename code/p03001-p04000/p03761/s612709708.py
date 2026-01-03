import math
import fractions
import copy
import numpy as np

def ip():
    return int(input())
def iprow():
    return [int(i) for i in input().split()]
def ips():
    return (int(i) for i in input().split())
n = ip()
s = input()
scut = [s[i] for i in range(len(s))]
scut.sort()
if n == 1:
	print(''.join(scut))
	exit(0)
for i in range(n-1):
	s = input()
	sncut = [s[i] for i in range(len(s))]
	sncut.sort()
	nextline = []
	while len(sncut) and len(scut):
	  if sncut[0] == scut[0]:
	  	nextline.append(sncut[0])
	  	scut.pop(0)
	  	sncut.pop(0)
	  elif sncut[0] > scut[0]:
	  	scut.pop(0)
	  else: sncut.pop(0)
	scut = copy.copy(nextline)
print(''.join(nextline))