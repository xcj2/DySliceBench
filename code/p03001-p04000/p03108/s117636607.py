N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

ufs = [-1] * N

def ufs_root(a):
	if ufs[a] < 0:
		return a
	ufs[a] = ufs_root(ufs[a])
	return ufs[a]

def ufs_size(a):
	return -ufs[ufs_root(a)]

def ufs_same(a, b):
	return (ufs_root(a) == ufs_root(b))

def ufs_merge(a, b):
	if ufs_same(a, b):
		return
	hi, lo = ufs_root(a), ufs_root(b)
	if ufs_size(hi) < ufs_size(lo):
		hi, lo = lo, hi
	ufs[hi] += ufs[lo]
	ufs[lo] = hi

result = [(N * (N - 1)) // 2]
for a, b in AB[::-1]:
	a, b = a - 1, b - 1
	if ufs_same(a, b):
		result += [result[-1]]
		continue
	result += [result[-1] - (ufs_size(a) * ufs_size(b))]
	ufs_merge(a, b)

for v in result[::-1][1:]:
	print(v)
