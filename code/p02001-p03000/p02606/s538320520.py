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
	l,r,d=lint()
	print(r//d-(l-1)//d)
	#code here
	return

#t=int(input())

########################################################
for i in range(t):                                     #
	#print("Case #"+str(i+1)+":",end=" ")		       #
	main()                                             #