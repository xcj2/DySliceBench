from math import factorial as fact
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

def combinations(n,r):
	return list(itertools.combinations(n,r))

def all_sets(num_list):
	subsets=[]
	for i in range(2,len(num_list) + 1):
		for c in combinations(num_list, i):
			subsets.append(c) 
	return subsets


def CountOneRoots(x,y):
	#x:縦，y:横
	return fact(x+y)/fact(x)/fact(y)



n=input1()
A=input_array()

result=[0 for _ in range(n)]
for i in range(n):
	result[A[i]-1]=str(i+1)
print(" ".join(result))


