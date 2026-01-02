import numpy as np

def main():
	n,a,b,c=map(int,input().split())
	l=[]
	for i in range(n):
		l.append(int(input()))
	
	key=[[0],[1],[2],[3]]
	key_4=key[:]
	for i in range(n-1):
		temp=[]
		for elem1 in key:
			for elem2 in key_4:
				temp.append(elem1+elem2)
		key=temp[:]

	res=10**9
	for elem in key:
		res=min(res,judge(elem,l,a,b,c))
	print(res)
	
def judge(key,l,a,b,c):
	num=[0,0,0,0]
	array=[0,0,0,0]
	for i in range(len(key)):
		array[key[i]]+=l[i]
		num[key[i]]+=1
	if(num[0]==0 or num[1]==0 or num[2]==0):
		return 10**9
	result=0
	result=abs(array[0]-a)+abs(array[1]-b)+abs(array[2]-c)
	result+=(num[0]+num[1]+num[2]-3)*10

	return result

def inputList():
	a=list(map(int,input().split()))
	return a

def multisort(li,index):
	return sorted(li,key=lambda x: x[index])

if(__name__=='__main__'):
	main()
