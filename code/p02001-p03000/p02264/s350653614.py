def getInput():
    (n, unit) = (int(i) for i in input().split(" "))
    q = []
    for i in range(n):
        tmp = [i for i in input().split(" ")]
        q.append([tmp[0], int(tmp[1])])
    return n, unit, q

def initQtable(Len_q):
    Q = [0 for i in range(Len_q+1)]
    return Q

def initPointer():
    head = tail = 0
    return head, tail

def isEmpty(head, tail):
    return head == tail

def isFull(head, tail, Len_q):
    return head == (tail+1)%Len_q

def enqueue(head, tail, Q, qname):
    Len_q = len(Q)
    if isFull(head, tail, Len_q):
        print("Error: Full Qtable")
        return
    tail = incrementPointer(tail, Len_q)
    Q[tail] = qname
    return tail
    
def dequeue(head, tail, Q):
    if isEmpty(head, tail):
        print("Error: Empty Qtable")
        return
    head = incrementPointer(head, Len_q+1)
    q = Q[head]
    return head, q

def incrementPointer(ptr, Len_q):
    ptr += 1
    if ptr >= Len_q:
        ptr = 0
    return ptr

n, unit, Jobs = getInput()
head, tail = initPointer()
Len_q = len(Jobs)
Q = initQtable(Len_q)
for i in range(Len_q):
    q = Jobs[i]
    tail = enqueue(head=head, tail=tail, Q=Q, qname=q)
total_time = 0
while not isEmpty(head, tail):
    head, [qname, time] = dequeue(head=head, tail=tail, Q=Q)
    progress = min(time, unit)
    total_time += progress
    time -= progress
    if time > 0:
        tail = enqueue(head=head, tail=tail, Q=Q, qname=[qname, time])
    else:
        print(qname, total_time, sep=" ")

