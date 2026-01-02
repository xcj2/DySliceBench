def gcd(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def cmp(x, y, l):
	if len(x) < len(y):
		x, y = y, x
	lx = int(l/len(x))
	ly = int(l/len(y))
	lc = lcm(lx,ly)
	lt = [i*lc for i in range(int(l/lc))]
	for i in lt:
		if i%lc == 0 and x[int(i/lx)] != y[int(i/ly)]:
			return False
	return True

def cmp2(x, y, l):
	if len(x) < len(y):
		x, y = y, x
	lx = int(l/len(x))
	ly = int(l/len(y))
	for i in range(l):
		if i%lx == 0 and i%ly == 0 and x[int(i/lx)] != y[int(i/ly)]:
			return False
	return True


if __name__ == '__main__':
	N, M = list(map(int, input().split()))
	S = input()
	T = input()
	L = lcm(N,M)
	if not cmp(S,T,L):
		print(-1)
	else:
		print(L)
