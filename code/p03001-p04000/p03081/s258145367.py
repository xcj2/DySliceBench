N, Q = map(int, input().split())
S = list(input())
TD = [tuple(input().split()) for _ in range(Q)]

def bs_l(f, s, e):
	if s==e:
		return s if f(s) else s+1

	c = (s+e)//2
	if f(c):
		#左
		return bs_l(f, s, c if c == s else c-1)
	else:
		#右
		return bs_l(f, c if c == e else c+1, e)

def bs_r(f, s, e):
	if s==e:
		return s if f(s) else s-1

	c = (s+e)//2
	if not f(c):
		#左
		return bs_r(f, s, c if c == s else c-1)
	else:
		#右
		return bs_r(f, c if c == e else c+1, e)

def isAlive(c):
	for t, d in TD:
		if S[c] == t:
			c += 1 if "R" == d else -1
			if c < 0 or N <= c:
				return False
	return True

S, E = bs_l(isAlive, 0, N-1), bs_r(isAlive, 0, N-1)
print(max(E-S+1, 0))
