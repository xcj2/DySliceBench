def list_input():
    return list(map(int,input().split()))
def map_input():
    return map(int,input().split())
def map_string():
    return input().split()
    
def solve(b):
	res = [0]*(len(b))
	m = max(b)
	#n-i-2+1 for 1s
	#n-i-2+1 for 2s
	#n-i-2+3 for 3s
	#n-i-2+m for ms
	c = []
	for i in range(len(b)):
		if b[i] == m:
			ind = len(b)-i-2+m
			if(ind < 0 or ind >= len(b)):
				print(-1)
				exit()
			res[ind] = m
		else:
			c.append(b[i])		
	if(c):
		bitch = solve(c)
		j = 0
		for i in bitch:
			while res[j] != 0:
				j += 1
			res[j] = i
	return res			


n = int(input())    
a = list_input()
ans = solve(a)      
for i in ans:
	print(i)