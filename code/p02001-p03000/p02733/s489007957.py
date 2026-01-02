H,W,K = map(int,input().split())
S = []
for i in range(H):
	s = list(map(int, list(input())))
	S.append(s)
A = [[0 for i in range(W+1)] for j in range(H+1)]
for i in range(H):
	for j in range(W):
		A[i+1][j+1] = A[i+1][j] + A[i][j+1] - A[i][j] + S[i][j]

def f(x1,y1,x2,y2):
	return A[x2][y2] - A[x1-1][y2] - A[x2][y1-1] + A[x1-1][y1-1]

if f(1,1,H,W) <= K:
	print(0)
	exit()

m = 100000

def int2bit(n):
	ret = [0 for i in range(H-1)]
	c = 0
	while n > 0:
		ret[c] = n % 2
		n = n // 2
		c += 1
	return ret

def getx1x2(b):
	ret = []
	x1 = 1
	for i in range(H-1):
		if b[i] == 1:
			ret.append((x1, i+1))
			x1 = i+2
	ret.append((x1, H))
	return ret

def check(x1x2):
	for y in range(1, W+1):
		for x1, x2 in x1x2:
			if(f(x1,y,x2,y) > K):
				return False
	return True

for i in range(2**(H-1)):
	x1x2 = getx1x2(int2bit(i))
	if not check(x1x2):
		continue
	cnt = len(x1x2) - 1
	y1 = 1
	for y2 in range(2, W+1):
		flag = False
		for x1, x2 in x1x2:
			if f(x1,y1,x2,y2) > K:
				flag = True
				break
		if flag:
			y1 = y2
			cnt += 1
	m = min(m, cnt)
print(m)