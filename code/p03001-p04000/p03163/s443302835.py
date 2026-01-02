import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main():
	#a = int(input())
	n, w = IN()
	#s = input()
	dp = [-1]*(w+1)
	dp[0]=0
	for _ in range(n):
		wi, vi = IN()
		for ri, v in enumerate(dp[::-1]):
			i=len(dp)-ri-1
			#print(i)
			if i + wi > w:
				continue
			if dp[i] >= 0:
				dp[i + wi] = max(dp[i+wi], dp[i]+vi)
		#print(dp)
	ret = max(dp)
	return ret
				
			
		
	
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)
		
def input_clipboard():
	import clipboard
	input_text=clipboard.get()
	input_l=input_text.splitlines()
	for l in input_l:
		yield l

if __name__ == "__main__":
	if sys.platform =='ios':
		if input_method==input_methods[0]:
			ic=input_clipboard()
			input = lambda : ic.__next__()
		elif input_method==input_methods[1]:
			sys.stdin=open('inputFile.txt')
		else:
			pass
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)