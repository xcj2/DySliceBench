######################################################
############Created by Devesh Kumar###################
#############devesh1102@gmail.com####################
##########For CodeForces(Devesh1102)#################
#####################2020#############################
######################################################
import sys
input = sys.stdin.readline

# import sys
import heapq 
import copy
import math
import decimal
# import sys.stdout.flush as flush
# from decimal import *
#heapq.heapify(li) 
#
#heapq.heappush(li,4) 
#
#heapq.heappop(li)
#
# &	Bitwise AND Operator	10 & 7 = 2
# |	Bitwise OR Operator	10 | 7 = 15
# ^	Bitwise XOR Operator	10 ^ 7 = 13
 
# <<	Bitwise Left Shift operator	10<<2 = 40
# >>	Bitwise Right Shift Operator
# '''############ ---- Input Functions ---- #######Start#####'''
 

def inp():
	return(int(input()))
def inlt(): 
	return(list(map(int,input().split())))
def insr():
	s = input()
	return(list(s[:len(s) - 1]))
def insr2():
	s = input()
	return((s[:len(s) - 1]))
def invr():
	return(map(int,input().split()))
 ############ ---- Input Functions ---- #######End
 # #####   

def pr_list(a):
	print(*a, sep=" ")
def main():
	# tests =  inp()
	tests = 1
	mod = 1000000007
	limit = 10**18
	ans = 0
	start = {}
	def pre(arr):
		ans = [arr[0]]
		for i in range(1,len(arr)):
			ans.append((ans[-1] + arr[i])%mod)
		return ans
	for test in range(tests):
		[n,k] = inlt()
		a = inlt()
		dp = [[0 for j in range(k+1)] for i in range(n)]
		for i in range(0,a[0]+1):
			dp[0][i] = 1
		pre_sum = pre(dp[0])
		for i in range(1,n):
			for j in range(0,k+1):
				lower = max(j - a[i],0)
				dp[i][j] = (pre_sum[j] - pre_sum[lower] + dp[i-1][lower])%mod
			pre_sum = pre(dp[i])
		# print(dp)
		print(dp[-1][-1]) 

				





		
		


if __name__== "__main__":
	main()