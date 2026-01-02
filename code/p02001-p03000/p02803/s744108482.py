def main():
	maximum = 0
	global h, w
	h, w = map(int, input().split())
	street = [[True if z=="." else False for z in input()] for y in range(h)]
	for y in range(h):
		for x in range(w):
			if get(x, y, street):
				r = bfs(x, y, [i[::] for i in street])
				# print(f"x: {x} and y: {y} and r: {r} and max: {maximum}")
				# print(street)
				maximum = max(maximum, r)
	print(maximum)
	return		

def get(x, y, l):
	return l[y][x]

def setter(x, y, z, l):
	l[y][x] = z

def bfs(x, y, visited):
	queue = [(x, y, 0)]
	maximum = 0
	setter(x, y, False, visited)
	for x, y, d in queue:
		if x>0 and get(x-1, y, visited):
			queue.append((x-1, y, d+1))
			setter(x-1, y, False, visited)
		if x<w-1 and get(x+1, y, visited):
			queue.append((x+1, y, d+1))
			setter(x+1, y, False, visited)
		if y>0 and get(x, y-1, visited):
			queue.append((x, y-1, d+1))
			setter(x, y-1, False, visited)
		if y<h-1 and get(x, y+1, visited):
			queue.append((x, y+1, d+1))
			setter(x, y+1, False, visited)
		maximum = max(maximum, d)
	return maximum



main()