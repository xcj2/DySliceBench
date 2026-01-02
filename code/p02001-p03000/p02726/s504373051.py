
#####

import numpy as np
# from collections import Counter
# import itertools

#####

def getIntList(inp):
	return [int(_) for _ in inp]


from sys import stdin
import sys
sys.setrecursionlimit(10**8)

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs


def main(inputs):
	n,x,y=getIntList(inputs[0])
	
	count=np.zeros(n-1, np.int32)
	
	between=y-x-1
	if between%2==0:
		middleL=between//2
		middleR=between//2
	else:
		middleL=between//2+1
		middleR=between//2
	left=x-1
	right=n-y
	
	depth0=x+middleL
	depth1=x+middleR+1
	depth2=x+right+1
	length=max(depth0,depth1,depth2)
	numDepth=np.zeros(length)
	numDepth[:x]=1
	numDepth[x:depth0]+=1
	numDepth[x:depth1]+=1
	numDepth[x+1:depth2]+=1
	
	for d in range(1, length):
		count[d-1]=numDepth[d:d+x-1].sum()
# 	print("a",count)
# 	count[...]=0 ###
	
	x0=x
	y0=y
	
	x=n-(y0-1)
	y=n-(x0-1)
	
	between=y-x-1
	if between%2==0:
		middleL=between//2
		middleR=between//2
	else:
		middleL=between//2+1
		middleR=between//2
	left=x-1
	right=n-y
	
	depth0=x+middleL
	depth1=x+middleR+1
	length=max(depth0,depth1)
	numDepth=np.zeros(length)
	numDepth[:x]=1
	numDepth[x:depth0]+=1
	numDepth[x:depth1]+=1
# 	print(numDepth)
	
	for d in range(1, length):
		count[d-1]+=numDepth[d:d+x-1].sum()
# 	print("b",count)
# 	count[...]=0 ###
	
	middle=middleL+middleR+2
	if middle%2==1:
		count[:middle//2]+=middle
	else:
		count[:middle//2-1]+=middle
		count[middle//2-1]+=middle//2
# 	print("c", count)
	
	for c in count: print(c)
	
# 	return count


if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
