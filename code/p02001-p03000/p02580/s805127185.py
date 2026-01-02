from collections import defaultdict
from collections import deque
from collections import Counter
import math

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

h,w,m = readInts()
countx = defaultdict(set)
county = defaultdict(set)
cx,cy = defaultdict(int),defaultdict(int)
for i in range(m):
	x,y = readInts()
	countx[x].add(y)
	county[y].add(x)
	cx[x]+=1
	cy[y]+=1

maxxv = max(cx.values())
maxyv = max(cy.values())
maxxi = [i for i in countx if len(countx[i])==maxxv]
maxyi = [i for i in county if len(county[i])==maxyv]

ans = maxyv+maxxv

for i in maxxi:
	for j in maxyi:
		if j not in countx[i]:
			print(ans)
			exit()

print(ans-1)