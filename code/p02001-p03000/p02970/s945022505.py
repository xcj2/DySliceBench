from math import factorial as fact
import math
import sys
import itertools
import numpy as np
from collections import Counter
import datetime
from collections import deque


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
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
	
def count_str(m):
	tmp={}
	for i in range(10):
		if i in tmp:
			tmp[i]=1
		else:
			tmp[i]+=1
	return tmp

def is_prime(n):
	if n==1: return True

	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return False
	return True


n,d=input2()

print(math.ceil(n/(d*2+1)))



