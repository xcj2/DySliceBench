dbflag=""

def debug(*args):
  if ""!=dbflag: print(*args)

if ""!=dbflag: _INDATA=open(dbflag)

def readline():
  if ""!=dbflag:return _INDATA.readline()
  else: return input()


result = -1

N = int(readline())



import numpy as np

A1 = [int(i) for i in readline().split(' ')]
A2 = [int(i) for i in readline().split(' ')]
data = np.zeros((2,N),dtype=int)
data[0,0:N]=A1
data[1,0:N]=A2

#np.reshape(data,[2,N])

memo = np.zeros((2,N), dtype=int)
score = np.zeros((2,N), dtype=int)


def getScore(i,j):
	if i < 0 or j < 0 : return 0
	
	if memo[i,j]: return score[i,j]
	
	x= data[i,j] + max(getScore(i-1,j) ,  getScore(i,j-1))
	memo[i,j]=1
	score[i,j]=x
	return x

result = getScore(1,N-1)
print(result)
