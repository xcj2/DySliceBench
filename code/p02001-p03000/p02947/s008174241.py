import operator as op
from functools import reduce
import math
	

def ncr(n, r):
	if n < r:
		return 0
	else :
		return (math.factorial(n)) / (math.factorial(n-r)*math.factorial(r))

def countPairs(str_arr, N):
	str_cnt = [0]
	str = str_arr[0]
	j = 0
	for i in range(N):
		if(str_arr[i]==str):
			str_cnt[j] += 1
		else:
			str = str_arr[i]
			j += 1
			str_cnt.append(0)
			str_cnt[j] += 1
	count = 0
	for i in range(len(str_cnt)):
		count += ncr(str_cnt[i],2)
	print(int(count))

def main():
	N = int(input())
	str_arr = []
	for i in range(N):
		str = input()
		str_arr.append(sorted(str))
	str_arr = sorted(str_arr)
	countPairs(str_arr, N)


main()