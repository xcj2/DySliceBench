def ascend(anc, union, dist, rec):
	count = 0
	while anc != union[anc]:
		rec[count] = anc
		anc = union[anc]
		count += 1
	rec[count] = anc
	for i in range(count - 1, -1, -1):
		dist[rec[i]] += dist[rec[i + 1]]
		union[rec[i]] = anc
	return anc

def connect(l, r, d, union, dist, rec):
	l_anc = ascend(l, union, dist, rec)
	r_anc = ascend(r, union, dist, rec)
	if l_anc != r_anc:
		union[l_anc] = r_anc
		dist[l_anc] = dist[r] + d - dist[l]

def is_union(l, r, union, dist, rec):
	return ascend(l, union, dist, rec) == ascend(r, union, dist, rec)

def main():
	N, M = map(int, input().split())
	union = list(range(N + 1))
	dist = [0] * (N + 1)
	rec = [0] * (N + 1)
	for i in range(M):
		l, r, d = map(int, input().split())
		if is_union(l, r, union, dist, rec):
			if dist[r] + d != dist[l]:
				print("No")
				break
		else:
			connect(l, r, d, union, dist, rec)
	else:
		print("Yes")

if __name__ == "__main__":
	main()
