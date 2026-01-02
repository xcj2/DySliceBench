class Data:
    def __init__(self):
        self.name = ""
        self.time = -1
    def printdata(self,sum):
        print(self.name,sum)
    def datain(self,name,time):
        self.name = name
        self.time = int(time)

def enqueue(Q,x):
    global tail
    Q[tail] = x
    if(tail+1 == n+1):
        tail = 0
    else:
        tail += 1

def dequeue():
    global head
    if(head+1 == n+1):
        head = 0
    else:
        head += 1

n,q = map(int,input().split())
A = [Data()]
head = 0
tail = n
sum = 0

for i in range(n):
    d = list(map(str,input().split()))
    A.append(Data())
    A[i].datain(d[0],d[1])
A.append(Data()) #要素数1追加

while(head != tail):
    if(A[head].time - q > 0):
        A[head].time -= q
        enqueue(A,A[head])
        dequeue()
        sum += q
    else:
        sum += A[head].time
        A[head].printdata(sum)
        dequeue()
