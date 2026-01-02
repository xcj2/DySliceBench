N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

uft = [-1] * N
def uft_root(a):
	if uft[a] < 0:
		return a
	uft[a] = uft_root(uft[a])
	return uft[a]

def uft_same(a, b):
	return (uft_root(a) == uft_root(b))

def uft_size(a):
	return -uft[uft_root(a)]

def uft_merge(a, b):
	if uft_same(a, b):
		return
	hi, lo = uft_root(a), uft_root(b)
	if -uft[hi] < -uft[lo]:
		hi, lo = lo, hi
	uft[hi] += uft[lo]
	uft[lo] = hi

result = [(N * (N - 1)) // 2]
for a, b in AB[::-1]:
	a, b = a - 1, b - 1
	if uft_same(a, b):
		result += [result[-1]]
		continue
	result += [result[-1] - (uft_size(a) * uft_size(b))]
	uft_merge(a, b)

for l in result[::-1][1:]:
	print(l)
