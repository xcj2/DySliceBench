import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

dd={'R':0, 'G':1, 'B':2}



def other_c(a,b):
	if a in 'RG' and b in 'RG':
		return 'B'
	elif a in 'GB' and b in 'GB':
		return 'R'
	else:
		return 'G'

def main():
	n = int(input())
	s = list(input())
	zn=[0]*n
	cc=[zn[:], zn[:], zn[:]]
	cc[dd[s[-1]]][-1]=1
	for i in range(n-2,-1,-1):
		c=dd[s[i]]
		for ci in range(3):
			cc[ci][i]+=cc[ci][i+1]+(c==ci)
	#print(cc)
	count=0
	for i in range(n-2):
		ci=s[i]
		for j in range(i+1, n-1):
			if s[j]==ci:
				continue
			other = other_c(ci, s[j])
			ol=dd[other]
			add = cc[ol][j+1]
			if j + (j-i) < n and s[j+(j-i)]==other:
				add -= 1
			count+=add
	print(count)
			
			
	
		
		
	
	
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