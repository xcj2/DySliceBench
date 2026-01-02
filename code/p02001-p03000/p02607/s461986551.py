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

def main():
	n=aint()
	l=lint()
	ans=0
	for i in range(0,n,2):
		if l[i]%2:
			ans+=1
	print(ans)
	return

#t=int(input())

########################################################
for i in range(t):                                     #
	#print("Case #"+str(i+1)+":",end=" ")		       #
	main()                                             #