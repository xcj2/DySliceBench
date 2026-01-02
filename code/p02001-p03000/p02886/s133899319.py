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
d=input_array()
result=0
for i in range(n):
	tako=d[i]
	for j in range(i+1,n):
		result+=d[i]*d[j]
print(result)









