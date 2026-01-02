from sys import stdin,stdout                           #
import math                                            #
import heapq                                           #
                                                       #
t = 1                                                  #
def aint():                                            #
	return int(input().strip())                        #
def lint():                                            #
	return list(map(int,input().split()))              #
def fint():                                            #
	return list(map(int,stdin.readline().split()))     #
                                                       #	
########################################################
def f(n):
	if n==0:
		return 0
#	print(n)
	N=n
	cnt=0
	while(N):
		cnt+=N&1
		N>>=1
	return f(n%cnt)+1

def main():
	n=aint()
	x=input()
	c=x.count("1")
	if(c==0):
		for i in range(n):
			print("1")
		return
	elif(c==1):
		for i in range(n):
			if(x[i]=="1"):
				print(0)
			elif x[i]=="0":
				if x[n-1]=="1"or i==(n-1):
					print("2")
				else:
					print(1)
		return
	mod1=c+1
	mod2=c-1
	mul1=1
	mul2=1
	rem1=0
	rem2=0
	for i in range(n-1,-1,-1):
		if(x[i]=='1'):
			rem1=(rem1+mul1)%mod1
			rem2=(rem2+mul2)%mod2
		mul1=(2*mul1)%mod1
		mul2=(2*mul2)%mod2
	ans=[]
	mul1=1
	mul2=1
#	print(mod1,mod2)
#	print(rem1,rem2)
	for i in range(n-1,-1,-1):
		if(x[i]=='0'):
#			print("At index",i,"val",(rem1+mul1)%mod1)
			ans.append(f((rem1+mul1)%mod1)+1)
		else:
#			print("At index",i,"val",(rem2-mul2)%mod2)
			ans.append(f((rem2-mul2)%mod2)+1)
		mul1=(2*mul1)%mod1
		mul2=(2*mul2)%mod2
#	print("Ans:")
	for i in range(n-1,-1,-1):
		print(ans[i])
	return

#t=int(input())

########################################################
for i in range(t):                                     #
	#print("Case #"+str(i+1)+":",end=" ")		       #
	main()                                             #