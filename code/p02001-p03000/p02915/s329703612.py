from math import factorial as fact
import math
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
	return list(itertools.combinations(range(n),r))



def all_sets(num_list):
	subsets=[]
	for i in range(2,len(num_list) + 1):
		for c in combinations(num_list, i):
			subsets.append(c) 
	return subsets

#公約数の列挙
def ch(x1):
	cf=[]
	for i in range(2,math.sqrt(x1)+1):
		if x1 % i==0:
			cf.append(i)
	return cf

def CountOneRoots(x,y):
	#x:縦，y:横
	return fact(x+y)/fact(x)/fact(y)

# 素因数分解
def factorization(n):
	tmp=n
	count=0
	for i in range(2,int(n**0.5)+2):
		if tmp%i==0:
			cnt=0
			while tmp%i==0:
				cnt+=1
				tmp//=i
			count+=1
	if tmp!=1:
		count+=1

	return count
			




N=input1()

print(N**3)




