import sys

input_methods=['clipboard','file','key']
using_method=1
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

dd={}
def get_f(v):
	global dd
	if v == 0:
		return 0
		
	if v in dd:
		return dd[v]
	
	pn = bin(v).count('1')
	ret = 1+get_f(v % pn)
	dd[v] = ret
	return ret
	
def bb(n, s):
	saigo = int(s[-1])
	for i, c in enumerate(s[:-1]):
		if c == '0':
			print(get_f(saigo)+1)
		else:
			print(0)
			
	if saigo == 0:
		print(get_f(1)+1)
	else:
		print(0)
		

def main():
	n = int(input())
	#b , c = tin()
	s = input()
	sa=s[::-1]
	n_one=s.count('1')
	if n_one == 1:
		bb(n,s)
		return 
	#pa(n_one)
	#pa(s)
	amari_p = 0
	amari_n = 0
	for i, c in enumerate(sa):
		if c == '1':
			amari_p += pow(2,i,n_one+1)
			amari_n += pow(2,i,n_one-1)
			amari_p %= n_one+1
			amari_n %= n_one-1
		
	#pa(amari_p)
	#pa(amari_n)
	for i, c in enumerate(s):
		keta = n - i - 1
		if c == '1':
			ta = amari_n
			ta -= pow(2,keta,n_one-1)
			ta %= n_one-1
		else:
			ta = amari_p
			ta += pow(2, keta, n_one+1)
			#pa(('q',ta))
			ta %= n_one+1
		#pa((keta,pow(2,keta),ta))
		print(get_f(ta)+1)
		
		
	
		
	
	
	
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