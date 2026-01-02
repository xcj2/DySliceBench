import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

IN=lambda : map(int, input().split())
mod=1000000007

#+++++

def f1(ss):
	return (len(ss)-1)*9

def f2(ss):
	ll=len(ss)
	return (((ll-1)*(ll-2))//2)*9*9
	
def f3(ss):
	ll=len(ss)
	return (((ll-1)*(ll-2)*(ll-3))//6)*9*9*9
	
def fk1(ss):
	aa=int(ss[0])
	return aa+f1(ss)
	
def fk2(ss):
	aa=int(ss[0])
	ret=f2(ss)
	ret+=(aa-1)*f1(ss)
	for i, c in enumerate(ss):
		if i == 0:
			continue
		if int(c)>0:
			ret += fk1(ss[i:])
			break
	return ret
	
def fk3(ss):
	aa=int(ss[0])
	ret = f3(ss)
	ret += (aa-1)*f2(ss)
	for i, c in enumerate(ss):
		if i == 0:
			continue
		if int(c)>0:
			ret += fk2(ss[i:])
			break
	return ret	

def main():
	n = input()
	k = int(input())
	if k== 1:
		return fk1(n)
	elif k==2:
		return fk2(n)
	else:
		return fk3(n)
	
	
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