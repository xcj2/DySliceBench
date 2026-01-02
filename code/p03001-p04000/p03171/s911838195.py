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
	for test in range(tests):
		n = inp()
		a = inlt()
		pre =[a[0]]
		for i in range(1,n):
			pre.append(pre[-1] + a[i])
		dp = [[-1*sys.maxsize for j in range(n)] for i in range(n)]
		for i in range(n-1,-1,-1):
			dp[i][i] = a[i]
			for j in range(i+1,n,1):
				dp[i][j] = max( a[i] + (pre[j] - pre[i]) - dp[i+1][j] , a[j] + pre[j-1] - pre[i] + a[i]  - dp[i][j-1])
		# print(dp)
		print( 2*dp[0][n-1] - sum(a))
				





		
		


if __name__== "__main__":
	main()