
#####

import numpy as np
from numpy import newaxis, float32, float64, int32, int64, int16, int8, uint8, uint32, complex64, complex128

#####

def getIntList(inp):
	return [int(_) for _ in inp]
	

from sys import stdin

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs


def m(t0,x0,y0,t1,x1,y1):
	d=abs(x1-x0)+abs(y1-y0)
	dt=t1-t0
	if d>dt: return False
	dd=d-dt
	return dd%2==0


def main(inputs):
	n=int(inputs[0][0])
	print(int(np.ceil(n/2)))
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
	
