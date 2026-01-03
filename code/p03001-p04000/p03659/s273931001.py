import sys
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
input = sys.stdin.readline
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

# 二分探索 #
def nibutan(list,n):
	left = 0
	right = len(list)
	while left+1 != right:
		middle = (left+right)//2
		if list[middle] <= n:
			left = middle
		else:
			right = middle
	return right

N = I()
l = IL()
tmp = l[0]

suml = [tmp]
for i in range(1,N):
	tmp += l[i]
	suml.append(tmp)

num = suml[0]
ans = abs(suml[-1]-num*2)
for i in range(1,N-1):
	num = suml[i]
	ans = min(ans, abs( suml[-1] - num*2 ))

print(ans)