import sys

input_methods=['clipboard','file','key']
using_method=0
input_method=input_methods[using_method]

tin=lambda : map(int, input().split())
lin=lambda : list(tin())
mod=1000000007

#+++++

def modinv(a,m):
	b=m
	u=1
	v=0
	
	while b > 0:
		t = a //b
		a = a - (t * b)
		a,b = b,a
		u = u - (t * v)
		u,v=v,u
	
	u = u % m
	if u < 0:
		u+=m
	return u

size_l=(10**5)+5
kaijoy=[1]*(size_l)
inv = [0]*(size_l)
pre=1
for i,v in enumerate(kaijoy[1:], 1):
	pre *= i
	pre %= mod
	kaijoy[i]=pre

inv[-1] = modinv(kaijoy[-1], mod)
pre = inv[-1]
#print(pre*24)
for i, v in enumerate(inv[1:],1):
	pre *= (size_l-i)
	pre %= mod
	inv[-i-1]=pre
	
#print(kaijoy)
#print(inv)
#print([(v*s)%mod for v, s in zip(kaijoy, inv)])

def conv(n, k):
	if n < k:
		return 0
	
	global kaijoy
	global inv
	ret = kaijoy[n]
	ret *= inv[n-k]
	ret *= inv[k]
	return ret

def main():
	# = int(input())
	n, k = tin()
	#s = input()
	al = lin()
	al.sort()
	ret = 0
	
	for i in range(n-k+1):
		d= (al[-i-1] - al[i])*conv(n-i-1, k-1)
		#pa((d,kaijoy[max(0,n-i-1)],inv[k-1]))
		ret += d
		ret %= mod
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