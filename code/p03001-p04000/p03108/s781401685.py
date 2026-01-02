def main():
	n, m = map(int, input().split())
	bridge = [[0, 0]]*m
	for i in range(m):
		bridge[i] = list(map(int, input().split()))
	inconveniences = [0]*(m+1)
	inconveniences[m] = (n*(n-1))//2
	union_find = [[i, 0, 1] for i in range(n+1)]

	for i in range(m-1, -1, -1):
		if inconveniences[i+1] == 0:
			break
		if same(union_find, bridge[i][0], bridge[i][1]):
			inconveniences[i] = inconveniences[i+1]
			continue
		rx = root(union_find, bridge[i][0])
		ry = root(union_find, bridge[i][1])
		inconveniences[i] = inconveniences[i+1] - union_find[rx][2]*union_find[ry][2]
		unite(union_find, bridge[i][0], bridge[i][1])

	for i in range(1, m+1):
		print(inconveniences[i])

def root(union_find, val:int) -> int:
	if union_find[val][0] == val:
		return val
	return root(union_find, union_find[val][0])

def same(union_find, x:int, y:int) -> bool:
	rx = root(union_find, x)
	ry = root(union_find, y)
	return rx == ry

def unite(union_find, x:int, y:int):
	rx = root(union_find, x)
	ry = root(union_find, y)
	if rx == ry:
		return
	if union_find[rx][1] < union_find[ry][1]:
		union_find[rx][0] = ry
		union_find[ry][2] += union_find[rx][2]
	else:
		union_find[ry][0] = rx
		union_find[rx][2] += union_find[ry][2]
		if union_find[rx][1] == union_find[ry][1]:
			union_find[rx][1] += 1

if __name__ == '__main__':
    main()