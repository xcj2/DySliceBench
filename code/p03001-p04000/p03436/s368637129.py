dbflag=""

def next(b):
	result = []
	x,y = b
	if x -1 >= 0 and S[x-1,y]=='.' and depthS[x-1,y]== -1:
		result.append((x-1,y))
	if y -1 >= 0 and S[x,y-1]=='.' and depthS[x,y-1]== -1:
		result.append((x,y-1))
	if x +1 < H and S[x+1,y]=='.' and depthS[x+1,y]== -1:
		result.append((x+1,y))
	if y +1 < W and S[x, y+1]=='.' and depthS[x,y+1]== -1:
		result.append((x,y+1))
	
	return result

  
def debug(*args):
  if ""!=dbflag: print(*args)

if ""!=dbflag: _INDATA=open(dbflag)

def readline():
  if ""!=dbflag:return _INDATA.readline()
  else: return input()


result = -1

H, W = map(int, readline().split())

#２次元配列
import numpy as np

S= np.ndarray(shape=(H,W), dtype=object)

for i in range(0,H):
	S[i,0:W] =list(readline().rstrip())
	

wNum = S[S == "."].size
bNum = H * W - wNum

debug(H,W)
debug(S)
debug(wNum)



from collections import deque
queue = deque([])
#queue.append(A)
#queue.popleft()


depthS = np.full((H,W), -1, dtype=int)

depthS[0,0] = 0
queue.append((0,0))

while len(queue) > 0 and depthS[H-1,W-1]==-1:
	base = queue.popleft()
	baseDepth = depthS[base]

	debug("----")
	debug(base,baseDepth)
	debug("depthS")	
	debug(depthS)	


	neighbors = next(base)
	
	debug('depthS',depthS)
	for n in neighbors: depthS[n[0],n[1]]=baseDepth + 1

	debug('depthS2',depthS)
	debug('neighbors',neighbors)
	
	for n in neighbors:
		queue.append(n)
	debug("queue",queue)	


if depthS[H-1,W-1]!=-1:
	result = wNum - (depthS[H-1,W-1] + 1)
else:
	result = -1

print(result)


