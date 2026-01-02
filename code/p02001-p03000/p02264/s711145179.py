n, q = map(int,input().split())
Q = [0]*(n+1)
head = 0
tail = 0

def enqueue(x):
    global tail
    global Q

    Q[tail] = x
    tail += 1
    if tail == n+1:
        tail = 0

def dequeue():
    global Q
    global head

    X = Q[head]

    head += 1
    if head == n+1:
        head = 0

    return X

def main():
    global n
    global q
    global Q
    global tail
    global head

    time = 0
    cnt = 0

    que = [list(input().split()) for _ in range(n)]
    for i in range(n):
        enqueue(que[i])

    while True:
        temp = dequeue()
        if int(temp[1]) <= q:
            time += int(temp[1])
            print(temp[0] + ' ' + str(time))
            cnt += 1
        else:
            time += q
            temp[1] = str( int(temp[1]) - q )
            enqueue( temp )

        if cnt == n:
            break

main()

