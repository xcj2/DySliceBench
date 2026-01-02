
#####

import numpy as np
# from numpy import int32, int8
# from collections import deque

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
	h,w=getIntList(inputs[0])
	colors=np.empty((h,w),np.bool)
	for hi in range(h):
		for wi in range(w):
			colors[hi,wi]=inputs[1+hi][0][wi]=="."

# 	h=20
# 	w=20
# 	np.random.seed(0)
# 	colors=np.random.randint(0,2,(h,w))

# 	from matplotlib import pyplot as plt
# 	for hi in range(h):
# 		for wi in range(w):
# 			plt.annotate(str((hi,wi)), (wi-0.5,hi), color="g")
# 	plt.imshow(colors)
# 	plt.show()
			
# 	print(colors.astype(np.int32))
	
	flipSize=np.empty((h,w), np.int32)
	
	if colors[0,0]: flipSize[0,0]=0
	else: flipSize[0,0]=1
	
	for hi in range(h):
		for wi in range(w):
			if hi==0 and wi==0: continue
			c=colors[hi,wi]
			fs=[]
			if hi>0:
				d=int(colors[hi-1,wi] and (not c))
				s=flipSize[hi-1, wi]+d
				fs.append(s)
				
			if wi>0:
				d=int(colors[hi,wi-1] and (not c))
				s=flipSize[hi, wi-1]+d
				fs.append(s)
			
			fs=min(fs)
			flipSize[hi,wi]=fs
	
	print(flipSize[h-1,w-1])
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)

