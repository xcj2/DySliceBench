import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
LIN=lambda : list(IN())
mod=1000000007

#+++++

def main2():
	#a = int(input())
	#b , c = IN()
	s =  input()
	#s='1'*3000
	s=[int(c) for c in s]
	ll=len(s)
	ret_count=0
	for i in range(1):#ll-2):
		v = s[i]
		vs=[v]
		for c in s[i+1:]:
			v = (v * 10 + c) % 2019
			vs.append(v)
			if v == 0:
				ret_count += 1
		else:
			pa(vs)	
	print(ret_count)
				
def main():
	#a = int(input())
	#b , c = IN()
	s =  input()
	#s='1'*3000
	s=[int(c) for c in s]
	s=s[::-1]
	ll=len(s)
	cc=[0]*2019
	p=0
	tt=1
	cc[0]=1
	for i, v in enumerate(s):
		tt *= 10
		tt %= 2019
		p += tt*v
		p %= 2019
		cc[p] += 1
	
	ret = 0
	for v in cc:
		ret += v *(v-1)//2
	print(ret)	
	
	
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