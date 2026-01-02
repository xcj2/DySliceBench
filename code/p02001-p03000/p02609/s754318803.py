import sys
#input = sys.stdin.buffer.readline

#sys.setrecursionlimit(10**9)
#from functools import lru_cache

def RD(): return sys.stdin.read()
def II(): return int(input())
def MI(): return map(int,input().split())
def MF(): return map(float,input().split())
def LI(): return list(map(int,input().split()))
def LF(): return list(map(float,input().split()))
def TI(): return tuple(map(int,input().split()))
# rstrip().decode()

def main():
	n=II()

	a=[0]*(2*10**5+100)
	for i in range(1,2*10**5+50):
		b=bin(i).count("1")
		a[i]=a[i%b]+1
	#print(a)

	s=input()
	c=s.count("1")
	#print(c)

	if c==1:
		ans=[]
		for i,ss in enumerate(reversed(s)):
			if ss=="1":
				ans.append(0)
			else:
				if s[-1]=="1" or i==0:
					ans.append(2)
				else:
					ans.append(1)

		for i in reversed(ans):
			print(i)
		exit()


	p=c+1
	n=c-1
	pp=0
	nn=0

	for i,ss in enumerate(reversed(s)):
		#print(i)
		if ss=="1":
			pp+=pow(2,i,p)
			nn+=pow(2,i,n)
			pp%=p
			nn%=n


	ans=[]

	for i,ss in enumerate(reversed(s)):
		if ss=="0":
			k=pp+pow(2,i,p)%p
			k%=p
			ans.append(a[k]+1)
		else:
			k=nn-pow(2,i,n)%n
			k%=n
			ans.append(a[k]+1)

	for i in reversed(ans):
		print(i)






if __name__ == "__main__":
	main()
