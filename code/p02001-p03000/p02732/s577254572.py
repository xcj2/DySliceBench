

#####

import numpy as np
# from numpy import int64, int8
from collections import Counter

#####

def getIntList(inp):
	return [int(_) for _ in inp]


from sys import stdin
# import sys
# sys.setrecursionlimit(10**8)

def getInputs():
	inputs=[]
	for line in stdin:
		line=line.split()
		inputs.append(line)
	return inputs


def unique(x):
	count=Counter()
	for xi in x:
		count[xi]+=1
	u,c=zip(*count.items())
	return u,c



def main(inputs):
	n=int(inputs[0][0])
	aa=getIntList(inputs[1])

# 	n=200000
# 	aa=np.random.randint(1,n+1,n)
	
# 	print("start")
# 	aa=np.array(aa)
# 	aUnique, count=np.unique(aa, return_counts=True)

	aUnique, count=unique(aa)
	aUnique=np.array(aUnique, np.int64)
	count=np.array(count, np.int64)
	
# 	print(n)
# 	print("aa",aa)
# 	print("aUnique",aUnique)
# 	print("count  ",count)
	
# 	countUnique,countCount=np.unique(count, return_counts=True)
	countUnique,countCount=unique(count)
	countCount=np.array(countCount, np.int64)
	
	pat={}
	countAns=np.empty(len(countUnique), np.int64)
	countAns1=np.empty(len(countUnique), np.int64)
	for ci,c in enumerate(countUnique):
		if c not in pat:
			ni=c*(c-1)//2
			pat[c]=ni
		countAns[ci]=pat[c]
		
		c-=1
		if c not in pat:
			ni=c*(c-1)//2
			pat[c]=ni
		countAns1[ci]=pat[c]
	
# 	print("countUnique",countUnique)
# 	print("countCount ",countCount)
# 	print("countAns ",countAns)
# 	print("countAns1",countAns1)
	
	countUniqueIndex=dict([(c,i) for i,c in enumerate(countUnique)])
# 	print("countUniqueIndex", countUniqueIndex)
	
# 	uniNums=np.empty(len(aUnique), np.int64)
	nums=np.empty(n, np.int64)
	ans={}
	for cui,cu in enumerate(countUnique):
		countCount[cui]-=1
		num0=(countAns*countCount).sum()
		countCount[cui]+=1
		num1=countAns1[cui]
		num=num0+num1
# 		print(cu,num)
		countMask=count==cu
# 		uniNums[countMask]=num
		targetA=aUnique[countMask]
# 		print(targetA)
		for a in targetA:
			ans[a]=num
# 		print(targetA[None,:])
# 		print(aa[:,None])
# 		aMask=(aa[:,None]==targetA[None,:]).any(axis=1)
# 		print(aMask)

# 		nums[aMask]=num
# 	print("\n".join(map(str,nums)))

	for a in aa:
		print(ans[a])
	

if __name__=="__main__":
	inputs=getInputs()
# 	inputs=simInputs()
	main(inputs)
