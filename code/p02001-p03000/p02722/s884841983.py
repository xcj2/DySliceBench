import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def ccc(v, k):
	while v >= k:
		if v % k == 0:
			v = v // k
		else:
			v = v % k
	return v

def cccc(v,k):
	while v >= k:
		if v % k == 0:
			v = v //k
		else:
			v = v-k
	return v


def main_p(n):
	s = n#int(input())
	#b , c = tin()
	#s = input()
	if s == 2:
		return 1
	elif s == 3:
		return 2
	
	ret = 1  #s-1, 1は範囲外なので。
	for i in range(2, s-1):
		if i*i > s+1:
			break
		if (s-1) % i == 0:
			ret += 1 if i*i == s-1 else 2
			
	ret += 1 #s
	for i in range(2, s):
		if i*i > s+1:
			break
			
		if s % i == 0:
			if ccc(s, i) == 1:
				ret += 1
			oi = s // i
			if oi != i and ccc(s, oi) == 1:
				ret += 1
			
	return ret#print(ret)
	
		
def main():
	n = int(input())
	return main_p(n)

def main_g(n):
	ret = 0
	for i in range(2, n+1):
		if cccc(n, i) == 1:
			ret += 1
	return ret


def maint():
	i=2
	p=0
	g=0
	while p == g:
		p=main_p(i)
		g=main_g(i)
		i+=1
		if p==g:
			print('ok', i-1)
	print(i-1,p,g)
	
	
	
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