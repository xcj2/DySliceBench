def enqueue(x, queue):
    queue.append(x)
    return queue
def dequeue(queue):
    val = queue.pop(0)
    return val, queue

def isEmpty(queue):
    return queue!=[]
        
def work(q, process):
    process[1] = process[1] - q
    return process
    
n, q = map(int, input().split())
process = [input().split() for _ in range(n)]
process = [[one[0], int(one[1])] for one in process]
queue = process.copy()

time = 0
while isEmpty(queue):
    process, queue = dequeue(queue)
    process = work(q, process)
    if process[1]<=0:
        worktime = q+process[1]
        print(process[0]+ ' ' +str(time+worktime))
        time += worktime
    else:
        queue = enqueue(process, queue)
        time += q
