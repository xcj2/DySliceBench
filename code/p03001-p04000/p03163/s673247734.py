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
		[n,w] = inlt()
		val = []
		for i in range(n):
			a = inlt()
			val.append(a)
		dp = [[-1 for i in range(w+3)]for j in range(2)]
		dp[0][0] = 0
		ans = 0
		for i in range(n):
			
			for j in range(w+3):
				dp[(i+1)%2][j] = max(dp[(i+1)%2][j],dp[(i)%2][j])
				if dp[i%2][j] != -1 and j + val[i][0]<=w:
					dp[(i+1)%2][j+val[i][0]] = max(	dp[(i)%2][j+val[i][0]] , 	dp[(i)%2][j] + val[i][1])
					ans = max(ans,dp[(i+1)%2][j+val[i][0]] )
		print(ans)

if __name__== "__main__":
	main()