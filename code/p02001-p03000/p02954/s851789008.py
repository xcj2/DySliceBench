direction = input()

def next(direction, current):
	output = [0] * len(current)

	for i in range(len(direction)):
		if direction[i] == 'R':
			output[i+1] += current[i]
		if direction[i] == 'L':
			output[i-1] += current[i]

	return output

def s(inp):
	r = len([x for x in inp if x == 'R'])
	l = len([x for x in inp if x == 'L'])

	R = L = 0
	for i in range(0, r, 2):
		R += 1
	for i in range(1, r, 2):
		L += 1
	for i in range(0, l, 2):
		L += 1
	for i in range(1, l, 2):
		R += 1
	
	output = [0 for _ in range(len(inp))]
	output[r-1] = R
	output[r] = L
	return output

def solve(inp):
	r = len([x for x in inp if x == 'R'])
	l = len([x for x in inp if x == 'L'])

	output = [0] * len(inp)
	if r == l:
		output[r-1] = output[r] = r
	else:
		m = max(l-1, r-1)
		if m % 2 == 1:
			output[r-1] = r
			output[r] = l
		else:
			output[r-1] = l
			output[r] = r
		


def solve(direction, start, end, output):
	original = [1] * (end-start)

	sub_direction = direction[start:end]

	prev2 = next(sub_direction, original)
	prev1 = next(sub_direction, prev2)

	count = 2

	output.append(s(direction[start:end]))

	# while True:
	# 	next_state = next(sub_direction, prev1)
	# 	count += 1
	# 	if next_state == prev2:
	# 		if count % 2 == 0:
	# 			output.append(prev2)
	# 			# print(' '.join(map(str, prev2)))
	# 			return
	# 		else:
	# 			output.append(prev1)
	# 			# print(' '.join(map(str, prev1)))
	# 			return
	# 	prev2 = prev1
	# 	prev1 = next_state

# direction = 'RRRLLRLLRRRLLLLL'
parts = []
prev = 0
for i in range(len(direction)-1):
	if direction[i] == 'L' and direction[i+1] == 'R':
		parts.append((prev,i+1))
		prev = i+1

parts.append((prev,len(direction)))

# print(parts)
output = []
for start,end in parts:
	solve(direction, start, end, output)

# print(output)
final = [x for  y in output for x in y]
print(' '.join(map(str, final)))


# print(solve('RRLRL'))
# print(solve('RRLLLLRLRRLL'))