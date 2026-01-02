# -*- coding: utf-8 -*-

def get_shortest_distance(field,locations,current_HP):
	is_visit = [[False for _ in range(len(field[0]))] for __ in range(len(field))]
	frontier = list([locations[current_HP-1]])
	for step in range(len(field)*len(field[0])):
		next_frontier = set()
		for cx,cy in frontier:
			for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
				nx, ny = cx+dx, cy+dy
				if (nx,ny)==locations[current_HP]: return step+1
				if not (0<=nx<len(field)):		continue
				if not (0<=ny<len(field[nx])):	continue
				if field[nx][ny]=='X':			continue
				if is_visit[nx][ny]: 			continue
				next_frontier.add((nx,ny))
				is_visit[nx][ny] = True
		frontier = next_frontier

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