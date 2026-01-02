import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def main2():
	n = int(input())
	#b , c = tin()
	#s = input()	
	mt=[input() for _ in range(n)]
	
	tt=[]
	for i in range(n):
		l=[]
		for s in mt:
			l.append(s[i])
		tt.append(''.join(l+l))
	pa(tt)
	ret = 0
	for ai in range(n):
		for s,t in zip(mt, tt):
			pa((s, t[ai:ai+n]))
			if t[ai:ai+n] != s:
				break
		else:
			ret += n
	return ret
	
def is_s(a,mt):
	pass
	#pa(a)
	n=len(mt)
	for i in range(n):
		for j in range(n):
			#pa((mt[i+a][j], mt[j][i+a]))
			if mt[(i+a)%n][j] != mt[(j+a)%n][i]:
				return False
	return True
	
def main():
	n = int(input())
	#b , c = tin()
	#s = input()	
	mt=[list(input()) for _ in range(n)]
	ret = 0
	for i in range(n):
		if is_s(i, mt):
			ret += n
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