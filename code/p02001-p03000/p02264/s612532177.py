def initialize():
    global head, tail


def isEmpty():
    global head, tail
    return head == tail


def isFull():
    global head, tail, MAX
    return head == (tail + 1) % MAX


def enqueue(x):
    global head, tail, Q, MAX
    if isFull():
        print("?????????????????????")
    else:
        Q[tail] = x
        if tail + 1 == MAX:
            tail = 0
        else:
            tail += 1


def dequeue():
    global head, tail, Q, MAX
    if isEmpty():
        print("??¢??????????????????")
    else:
        t = Q[head]
        if head + 1 == MAX:
            head = 0
        else:
            head += 1
        return t


if __name__ == "__main__":
    n, q = map(int, input().split())
    head = 0
    tail = n
    MAX = 100000
    Q = [0]*MAX
    runtime = 0
    for i in range(n):
        name, time = input().split()
        Q[i] = ([name, int(time)])
    while head != tail:
        t_list = dequeue()
        if t_list[1] > q:
            t_list[1] -= q
            runtime += q
            enqueue(t_list)
        else:
            runtime += t_list[1]
            t_list[1] = 0
            print(t_list[0] + " " + str(runtime))