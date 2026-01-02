def tail(x):
	s = str(x)
	a = int(s[0]); d = len(s)
	return x - a * 10 ** (d - 1)

def K1(N):
	s = str(N)
	a = int(s[0]); d = len(s)
	res = 9 * (d - 1) + a
	return res

def K2(N):
	s = str(N)
	a = int(s[0]); d = len(s)
	res = (d - 1) * (d - 2) // 2 * 81
	res += (a - 1) * (d - 1) * 9
	res += K1(tail(N))
	return res
	
def K3(N):
	s = str(N)
	a = int(s[0]); d = len(s)
	res = (d - 1) * (d - 2) * (d - 3) // 6 * 729
	res += (a - 1) * (d - 1) * (d - 2) // 2 * 81
	res += K2(tail(N))
	return res

N = int(input())
K = int(input())
if K == 1:
	ans = K1(N)
elif K == 2:
	ans = K2(N)
elif K == 3:
	ans = K3(N)

print(ans)