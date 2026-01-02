
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


def func(a,b,m,
	aValues,
	bValues,
	xs,
	ys,
	cs):
	
	aValues=np.array(aValues)
	bValues=np.array(bValues)
	
	mi=aValues.min()+bValues.min()
	for x,y,c in zip(xs,ys,cs):
		v=aValues[x]+bValues[y]-c
		if v<mi: mi=v
		
	print(mi)
	



def main(inputs):
	a,b,m=getIntList(inputs[0])
	aValues=getIntList(inputs[1])
	bValues=getIntList(inputs[2])
	xs=np.empty(m, int32)
	ys=np.empty(m, int32)
	cs=np.empty(m, int32)
	for i in range(m):
		xs[i],ys[i],cs[i]=getIntList(inputs[3+i])
	xs-=1
	ys-=1
	
# 	print(a,b,m)
# 	print(aValues)
# 	print(bValues)
# 	print(xs)
# 	print(ys)
# 	print(cs)

	func(a, b, m, aValues, bValues, xs, ys, cs)
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	