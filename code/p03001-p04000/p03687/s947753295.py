import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def is_all(list_s, c):
	for cs in list_s:
		if cs != c:
			return False
	return True

def dd(s, c):
	t=list(s)
	p=0
	while not is_all(t, c):
		nt=['']*(len(t)-1)
		for i, _ in enumerate(nt):
			if t[i]==c or t[i+1]==c:
				nt[i]=c
			else:
				nt[i]=t[i]
		t=nt
		p+=1
	return p
	
	

def main():
	#a = int(input())
	#b , c = tin()
	s = input()
	ret = mod
	for c in list(set(list(s))):
		#pa(c)
		r = dd(s, c)
		ret = min(ret, r)
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