def printg():
	for i in range(H+2):
		print(G[i])

def p(s):
	if s == '#':
		return True
	else:
		return False

def isok(i,j):
	u = p(G[i][j-1])
	r = p(G[i+1][j])
	d = p(G[i][j+1])
	l = p(G[i-1][j])
	if u or r or d or l:
		return True
	else:
		return False

if __name__ == '__main__':
	H,W = map(int,input().split())
	G = [['B']*(W+2) for _ in range(H+2)]

	for i in range(H):
		l = input()
		for j in range(W):
			G[i+1][j+1] = l[j]

	for i in range(H+1):
		for j in range(W+1):
			if G[i][j] == '#':
				if not isok(i,j):
					print('No')
					exit()

	print('Yes')