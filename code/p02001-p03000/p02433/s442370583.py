q = int(input())
A = [0 for i in range(1500000)]
A[0] = 'end'
cursor = 0
head = [0 for i in range(1500000)]
head_len = 0

def insert(x):
	global cursor
	cursor += 1
	A[cursor] = x
def move(d):
	global cursor, head, head_len
	if d >= 0:
		head[head_len-1+d+(1): head_len-1+(1):-1] = A[cursor-d+1:cursor+1]
	else:
		A[cursor+1:cursor+1+(-d)] = head[head_len-1+(1):head_len-(-d)-1+(1):-1]
	cursor -= d
	head_len += d
def erase():
	global cursor
	cursor -= 1

for i in range(q):
	a = input()
	if a != "2":
		b = [int(i) for i in a.split()]
		if b[0] == 0:
			insert(b[1])
		elif b[0] == 1:
			move(b[1])
	else:
		erase()
	#print(A[:cursor+1],head[1:1+head_len][::-1])

A[cursor+1:cursor+1+head_len] = head[head_len-1+(1):-1+(1):-1]
length = cursor +  head_len
for i in range(1,length+1)[::-1]:
	print(A[i])



