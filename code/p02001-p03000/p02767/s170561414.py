import math
import fractions
import sys
import itertools
import numpy as np
from collections import Counter
import datetime
#入力:N(int:整数)
def input1():
	return int(input())

#入力:N,M(int:整数)
def input2():
	return map(int,input().split())

#入力:[n1,n2,...nk](int:整数配列)
def input_array():
	return list(map(int,input().split()))

def keta(N):
	return len(str(N))


def input_daytime(input_time):
	time,distance=input_time.split()
	t=time.split(":")
	se=str(t[-1]).split(".")
	dt1 = datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(se[0]),milliseconds=int(se[1]))
	return dt1


n=input1()
X=input_array()

min_p=min(X)
max_p=max(X)
b_p=10000
p=[]
for i in range(min_p,max_p):
	s=0
	for j in X:
		s+=(j-i)**2
	p.append(s)
	# if s>b_p:
	# 	break
	# else:
	# 	b_p=s

if p==[]:
	print(0)
else:
	print(min(p))



