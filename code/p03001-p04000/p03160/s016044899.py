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
	mod = 998244353
	limit = 10**18
	ans = 0
	for test in range(tests):
		n = inp()
		h = inlt()
		dp = [sys.maxsize for i in range(n+3)]
		dp[0] = 0
		for i in range(0,n):
			if i+1 <n:
				dp[i+1] = min(dp[i+1],dp[i] + abs(h[i+1] - h[i]))
			if i+2 <n:
				dp[i+2] = min(dp[i+2],dp[i] + abs(h[i+2] - h[i]))
		print(dp[n-1])

if __name__== "__main__":
	main()