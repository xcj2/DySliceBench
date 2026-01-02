import sys
#from fractions import Fraction
import collections

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def a(s):
	if s.count('.')==0:
		n2=0
		n5=0
		v = int(s)
	else:
		p = s.index('.')
		n2 = -(len(s) - p - 1)
		n5 = -(len(s) - p - 1)
		if p == 1 and s[0]=='0':
			v= int(s[2:])
		else:
			v = int(s[:p]+s[p+1:])
	while v % 2 == 0:
		v = v//2
		n2+=1
	while v % 5 == 0:
		v = v//5
		n5+=1
	return str(n2)+'_'+str(n5)

def main():
	n = int(input())
	#b , c = tin()
	al = [a(input()) for _ in range(n)]
	cal = collections.Counter(al)
	#pa(cal)
	ret = 0
	pp = set()
	for k in cal:
		for k2 in cal:
			if k+'_'+k2 in pp:
				continue
			#pa((vi*vj)/(10**20))
			if k==k2:
				a2, a5 = map(int, k.split('_'))
				if a2>=0 and a5 >= 0:
					ret += cal[k]*(cal[k]-1)//2
			else:
				a2, a5 = map(int, k.split('_'))
				b2, b5 = map(int, k2.split('_'))
				if a2+b2 >= 0 and a5+b5 >= 0:
					ret += cal[k]*cal[k2]
				
			pp.add(k+'_'+k2)
			pp.add(k2+'_'+k)
			#pa((k,k2,ret))
			
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