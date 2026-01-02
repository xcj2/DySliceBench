
from sys import stdin
import sys
sys.setrecursionlimit(10**8)

def nextLine(): return next(stdin)
def nextStrList(): return nextLine().split()
def nextIntList(): return [int(_) for _ in nextStrList()]


def main():
	k=nextIntList()[0]
	if k<=9:
		print(k)
		sys.exit(0)
	num=[0,1]
	for i in range(10, k):
# 		print(num)
		if all([n==9 for n in num]):
			num=[0 for d in range(len(num))]
			num.append(1)
			continue
		
		for di in range(len(num)):
			if di==0:
				if num[di]<=num[di+1] and num[di]<9:
					num[di]+=1
					break
			elif di<len(num)-1:
				if num[di]<=num[di+1] and num[di]<9 and num[di]<=num[di-1]:
					num[di]+=1
					break
			else: #di==len(num)-1
				num[di]+=1
	
		for dii in range(di-1, -1,-1):
			if num[dii+1]==0:
				num[dii]=0
			else:
				num[dii]=num[dii+1]-1 
	
	print("".join(str(n) for n in reversed(num)))

if __name__=="__main__":
	main()
