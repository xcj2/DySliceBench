import sys
bbn=1000000007
	
#+++++
#knight
#https://atcoder.jp/contests/abc145/tasks/abc145_d


def kk(n,a_mod=1):
	ret=1
	for i in range(1, n+1):
		ret = (ret * i) % a_mod
	return ret
	
def pp(n,m,a_mod=1):
	ret=1
	for i in range(m):
		ret *= n - i
		ret = ret % a_mod
	return ret

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
	
def cnv(a_total, a_sub,a_mod):
	ret = pp(a_total,a_sub,a_mod)
	ww = kk(a_sub,a_mod)
	ret *= modinv(ww,a_mod)
	ret %= a_mod
	return ret
	
	

def main():
	x,y = map(int, input().split())
	if (x+y)%3!=0:
		return 0
	
	if x > y:
		x,y=y,x
	
	if x*2 < y:
		return 0
	
	turn = (x+y)//3
	xp2=x-turn
	return cnv(turn, xp2, bbn)
	
	
#+++++
isTest=False

def pa(v):
	if isTest:
		print(v)

if __name__ == "__main__":
	if sys.platform =='ios':
		sys.stdin=open('inputFile.txt')
		isTest=True
	else:
		pass
		#input = sys.stdin.readline
			
	ret = main()
	if ret is not None:
		print(ret)