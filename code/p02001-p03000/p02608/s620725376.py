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
l=[0]*100000
for x in range(1,100):
	for y in range(1,100):
		for z in range(1,100):
			l[x*x+y*y+z*z+x*y+x*z+y*z]+=1
def main():
	n=aint()
	for i in range(1,n+1):
		print(l[i])
	return

#t=int(input())

########################################################
for i in range(t):                                     #
	#print("Case #"+str(i+1)+":",end=" ")		       #
	main()                                             #