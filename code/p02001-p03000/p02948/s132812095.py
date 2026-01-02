import math

n, m = map(int, input().split())

jobs = []
for i in range(n):
	day, reward = map(int, input().split())
	if m- day + 1 > 0:
		jobs.append((m - day + 1, reward))

jobs.sort(key = lambda x:(-x[1],-x[0]))

def find(i):
	global parent
	while i != parent[i]:
		parent[i] = parent[parent[i]]
		i = parent[i]
	return i 

def union(x, y):	# small, big
	global parent
	parent_x = find(x)
	parent_y = find(y)
	parent[parent_y] = parent_x

parent = [i for i in range(m+1)]

def job_sequencing(jobs):
	global parent 
	n = len(jobs)

	total_rewards = 0
	for job in jobs:
		available_slot = find(job[0])
		if available_slot > 0:
			union(available_slot-1, available_slot)
			total_rewards += job[1]
	return total_rewards
print(job_sequencing(jobs))