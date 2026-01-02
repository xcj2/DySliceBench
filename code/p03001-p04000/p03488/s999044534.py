import sys
input = sys.stdin.buffer.readline

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
	s=input().rstrip().decode()+"T"
	x,y=MI()
	X=[]
	Y=[]

	i=0

	if s[0]=="F":
		for ss in s:
			if ss=="F":
				x-=1
				i+=1
			else:
				break
	#print(x,y,i)

	while True:
		ii=s.find("T",i+1)
		if ii==-1:
			break
		Y.append(ii-i-1)

		i=s.find("T",ii+1)
		if i==-1:
			break
		X.append(i-ii-1)
	#print(X,Y)


	s=set([0])
	ss=set()
	for i in X:
		for j in s:
			ss.add(j+i)
			ss.add(j-i)
		s=ss.copy()
		ss=set()
		#print(i,s,ss)
	#print(s)

	if x not in s:
		print("No")
		exit()

	s=set([0])
	ss=set()
	for i in Y:
		for j in s:
			ss.add(j+i)
			ss.add(j-i)
		s=ss.copy()
		ss=set()
	#print(s)

	if y not in s:
		print("No")
		exit()

	print("Yes")






















if __name__ == "__main__":
	main()
