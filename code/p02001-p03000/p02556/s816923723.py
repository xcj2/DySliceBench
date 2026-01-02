from collections import defaultdict
from collections import deque
from collections import Counter
import math
import itertools

def readInt():
	return int(input())
def readInts():
	return list(map(int, input().split()))
def readChar():
	return input()
def readChars():
	return input().split()

n = readInt()
data = []
for i in range(n):
	x,y = readInts()
	data.append([x+y,x,y,x-y])
ans = 0
data.sort(key=lambda x:x[0])
ans = max(ans,abs(data[-1][1]-data[0][1])+abs(data[-1][2]-data[0][2]))
data.sort(key=lambda x:x[1])
ans = max(ans,abs(data[-1][1]-data[0][1])+abs(data[-1][2]-data[0][2]))
data.sort(key=lambda x:x[2])
ans = max(ans,abs(data[-1][1]-data[0][1])+abs(data[-1][2]-data[0][2]))
data.sort(key=lambda x:x[3])
ans = max(ans,abs(data[-1][1]-data[0][1])+abs(data[-1][2]-data[0][2]))
print(ans)