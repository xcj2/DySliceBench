from collections import deque, defaultdict

grid_size = 3

def generate_next_state(q, visited, current_state, zero_pos, dx, dy):
	r = zero_pos // grid_size
	c = zero_pos % grid_size
	next_state = current_state[:]
	next_r = r + dx
	next_c = c + dy
	if next_r < 0 or next_r >= grid_size:
		return None
	if next_c < 0 or next_c >= grid_size:
		return None
	next_state[next_r * grid_size + next_c], next_state[r * grid_size + c] = next_state[r * grid_size + c], next_state[next_r * grid_size + next_c]
	if visited.get(tuple(next_state)) is not None:
		return None
	q.append(next_state)

def bfs(initial_state, goal):
	visited = defaultdict()
	q = deque()
	q.append(initial_state)
	step = 0
	while(len(q) > 0):
		node_count = len(q)
		while(node_count > 0):
			current_state = q.popleft()
			visited[tuple(current_state)] = True
			# print(current_state)
			node_count -= 1
			if current_state == goal:
				print(step)
				return 0
			zero_pos = current_state.index(0)
			generate_next_state(q, visited, current_state, zero_pos, 0, -1)
			generate_next_state(q, visited, current_state, zero_pos, 0, 1)
			generate_next_state(q, visited, current_state, zero_pos, -1, 0)
			generate_next_state(q, visited, current_state, zero_pos, 1, 0)


		step += 1

def init():
	initial_state = []
	goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
	for i in range(grid_size):
		input_list = input().rstrip().split()
		initial_state.extend([int(val) for val in input_list])
	return initial_state, goal

initial_state, goal = init()
bfs(initial_state, goal)


