H, W = map(int, input().split())
STAGE = [list(input()) for _ in range(H)]

black, white = [], 0
for y, line in enumerate(STAGE):
	for x, cell in enumerate(line):
		if "#" == cell:
			black += [(y, x)]
		else:
			white += 1

stage = STAGE
ds = ((0, 1), (1, 0), (0, -1), (-1, 0))

def get_next(p, d):
	n = (p[0] + d[0], p[1] + d[1])
	if 0 <= n[0] < H and 0 <= n[1] < W:
		return n
	return None

def set_val(p, v):
	global stage
	stage[p[0]][p[1]] = v

def get_val(p):
	return stage[p[0]][p[1]]

count = 0
while white:
	count += 1
	next_black = []
	for b in black:
		for d in ds:
			n = get_next(b, d)
			if n:
				v = get_val(n)
				if "." == v:
					white -= 1
					set_val(n, "#")
					next_black += [n]
	black = next_black

print(count)
