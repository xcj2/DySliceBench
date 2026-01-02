# -*- coding: utf-8 -*-

def get_shortest_distance(field,locations,current_HP):
	is_visit = [[False for _ in range(len(field[0]))] for __ in range(len(field))]
	frontier = set()
	frontier.add(locations[current_HP-1])
	for step in range(10**10):
		for cx,cy in frontier:
			if (cx,cy)==locations[current_HP]: return step
			is_visit[cx][cy]=True
		next_frontier = set()
		for cx,cy in list(frontier):
			for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
				nx = cx+dx
				ny = cy+dy
				if not (0<=nx<len(field)):		continue
				if not (0<=ny<len(field[nx])):	continue
				if field[nx][ny]=='X':			continue
				if is_visit[nx][ny]: 			continue
				next_frontier.add((nx,ny))
#		assert len(next_frontier)!=0,(current_HP,is_visit,frontier)
		frontier = next_frontier
#	assert True,('the goal is not reachable')

def solve(field,locations):
	total_step=0
	for current_HP in range(1,len(locations)):
		total_step += get_shortest_distance(field,locations,current_HP)
	return total_step

def main():
	line=input().strip()
	H,W,N=list(map(int,line.split(' ')))
	field,locations=list(),dict()
	for i in range(H):
		field.append(list(input().strip()))
		for j,x in enumerate(field[-1]):
			if x=='S':
				locations[0] = (i,j,)
			if x.isdigit():
				x = int(x)
				field[-1][j] = x
				locations[x] = (i,j,)
	print(solve(field,locations))

if __name__=='__main__':
	main()