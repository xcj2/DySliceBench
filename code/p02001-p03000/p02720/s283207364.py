import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main():
	k = int(input())
	#b , c = tin()
	#s = input()
	l=['_']*50
	l[0]=0
	for _ in range(k):
		for i, v in enumerate(l):
			l[i]+=1
			if l[i] == 10 and l[i+1]=='_':
				l[i+1]=1
				l[:i+1]=[0]*(i+1)
				break
			elif l[i] == 10:
				l[i]=l[i+1]
			elif l[i+1]=='_':
				#l[:i]=[l[i]-1]*(i)
				for j in range(1,i+1):
					l[i-j]=max(0, l[i-j+1]-1)
				break				
			elif l[i] <= l[i+1]+1:
				#l[:i]=[l[i]-1]*i
				for j in range(1,i+1):
					l[i-j]=max(0, l[i-j+1]-1)
				break	
		#print(*l)
		
	print(''.join([str(c) for c in l[::-1] if c != '_']))
				
	
	
	
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