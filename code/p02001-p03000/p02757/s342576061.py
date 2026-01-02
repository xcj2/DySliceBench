
#####

import numpy as np
from numpy import newaxis, float32, float64, int32, int64, int16, int8, uint8, uint32, complex64, complex128

#####

def getIntList(inp):
	return [int(_) for _ in inp]


from sys import stdin
import sys

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs



def main(inputs):
	n,p=getIntList(inputs[0])
	s=inputs[1][0]
	
	ans=0
	if p%2==0 or p%5==0:
		for i0 in range(len(s)-1,-1,-1):
			sub=int(s[i0:i0+1])
			if sub%p==0:
				ans+=i0+1
	else:
		numP0=np.zeros(p, int32)
		numP0[0]=1
		r=0
		modD=int(1%p)
		for i0 in range(len(s)-1,-1,-1):
			
			sub=s[i0:i0+1]
			sub=int(sub)
			sub=r+sub*modD
			r=sub%p
			ans+=numP0[r]
			numP0[r]+=1
			modD=int((modD*10)%p)
	print(ans)
		
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	