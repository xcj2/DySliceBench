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
	def pre_sum(arr):
		ans = [arr[0]]
		for i in range(1,len(arr)):
			ans.append(ans[-1]+ arr[i])
		return ans
	for test in range(tests):
		n = inp()
		a = inlt()
		ans = 0
		dp = [[sys.maxsize for j in range(n)] for i in range(n)]
		pre = pre_sum(a)
		# print(pre)
		for i in range(n-1,-1,-1):
			dp[i][i] = 0
			for j in range(i+1,n,1):
				for k in range(i+1,j+1):
					dp[i][j] = min(dp[i][j] , dp[i][k-1] + dp[k][j] + pre[j] -pre[i] + a[i])
		# print(dp)
		print(dp[0][-1])



		
		


if __name__== "__main__":
	main()