import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	pp = [1]*(10**5 + 1)
	pp[0]=0
	pp[1]=0
	for i, _ in enumerate(pp):
		if pp[i]==0:
			continue
		st = i
		while st * i < len(pp):
			pp[st*i]=0
			st+=1
	like = pp[:]
	like[2]=0
	for i, v in enumerate(pp):
		
		if v == 1 and i != 2 and pp[(i+1)//2 ] == 0:
			like[i] = 0
	ss = [0] * len(pp)
	for i, v in enumerate(ss[:-1]):
		ss[i+1] = like[i+1]+ss[i]
	#pa(like[:10])
	q = int(input())
	#b , c = tin()
	#s = input()
	for _ in range(q):
		l, r = tin()
		print(ss[r] - ss[l-1])
	
	
	
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