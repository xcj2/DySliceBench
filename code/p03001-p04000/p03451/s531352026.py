#1st arg is the how far from the most upper side
#2nd arg is the how far from the most left side
#right means +1 in terms of x-axis
#upper means -1 in terms of y-axis

def Right(position):
	position[1] += 1

def Down(position):
	position[0] += 1 

def Collect(position,candy):
	x = position[0]
	y = position[1]
	total = 0
	total += candy[x][y]
	return total

N = int(input())
candy = []
while True:
    try:
        candy.append(list(map(int,input().split())))
    except:
        break;
position = [0,0]
score = 0
max_score = 0
k = 0
for t in range(N):
	score = candy[0][0]
	position[0] = 0
	position[1] = 0
	for i in range(N):
		if t == i:
			Down(position)
			score += Collect(position,candy)
		if i < N - 1:	
			Right(position)
			score += Collect(position,candy)
	if max_score < score:
		max_score = score
		k = t
print(max_score)


