import sys
from math import factorial as fc

if sys.platform =='ios':
	sys.stdin=open('inputFile.txt')
		
#+++++
bpn=(10**9)+7

def pat(num, bunkatsu):
	if num==0 and bunkatsu == 0:
		return 1
	
	if bunkatsu==0:
		return 0
		
	if num < bunkatsu:
		return 0
	
	if bunkatsu==1:
		return 1
	
	#numのものをbunkatsuに分ける場合の数を求める。
	c=num-1
	l=bunkatsu-1
	
	#print(c,l)
	cpl=fc(c)//(fc(c-l)*fc(l)) %bpn
	return cpl % bpn

def kk(nb,nr,i):
	ret=0
	a=pat(nb, i)%bpn
	#print(a)
	
	b=pat(nr, i+1)%bpn
	#print(b,nr)
	ret+=(a*b) % bpn
	ret = ret % bpn
	
	c=pat(nr, i)%bpn
	ret += (a*c*2 )% bpn
	ret = ret % bpn
	
	d = pat(nr, i-1)%bpn
	ret += (a*d)% bpn
	ret = ret % bpn
	
	#print(a,b,c,d)
	
	return (ret % bpn)
	
def main():
	n, k = map(int, input().split())
	
	for i in range(1,k+1):
		print(kk(k,n-k,i))
	return

if __name__ == "__main__":
	main()
	#print(pat(10,4))
	