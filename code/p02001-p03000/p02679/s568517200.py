import sys
import math
from collections import defaultdict

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(IN())
mod=1000000007

#+++++

def mk(a,b):
	if a == 0:
		return 0,1
	if b==0:
		return 1,0
		
	c = -1 if a < 0 else 1
	r = math.gcd(abs(a),abs(b))
	ra = (a //r)*c
	rb = (b //r)*c
	
	return ra, rb
	
def mh(a,b):
	return str(a)+'_'+str(b)
	
def mv(s):
	a,b = map(int, s.split('_'))
	return a,b
	
def ty(s):
	a, b = mv(s)
	sign = 1 if b > 0 else -1
	return mh(b*sign, -a*sign)
	

def main():
	n = int(input())
	dd = defaultdict(lambda : 0)
	zero_fish_num=0
	for _ in range(n):
		a,b=tin()
		if a== 0 and b == 0:
			zero_fish_num += 1
			continue
		a,b = mk(a,b)
		dd[mh(a,b)] += 1
		
	cc = set()
	ret = 1
	for k in dd:
		if k in cc:
			continue
		v = dd[k]
		if ty(k) in dd:
			tv = dd[ty(k)]
			r = pow(2,v,mod)+pow(2,tv,mod)-1
			#pa((r,k, ty(k)))
			ret *= r
			ret %= mod
			cc.add(ty(k))
		else:
			#pa(('v',v,k, ty(k)))
			ret *= pow(2,v,mod)
			ret %= mod
			
	ret -= 1
	ret += zero_fish_num
	ret %= mod
	print(ret) 
			
		
		
	#b , c = tin()
	#s = input()
	
	
	
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