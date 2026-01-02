class P:
    def __init__(self,name,time):
        self.name = name
        self.time = time
n,q = map(int,input().split())
LEN = 100004 #要素数nより少し大きければよい
head = 0
tail = n
Q = [P("",0) for _ in range(LEN)]
for i in range(n):
    Q[i].name,ti = input().split()
    Q[i].time = int(ti)
def enqueue(Q,x,tail):#末尾にクラスPの要素xを加える。ぐるっと回った場合
    Q[tail] = x       #以前dequeueで取り出したものが書き換えられる。
    if tail+1 == LEN:
        tail = 0
    else:
        tail += 1
    return tail
def dequeue(Q,head):
    x = Q[head]
    if head+1 == LEN:
        head = 0
    else:
        head += 1
    return x,head
totime = 0
while head != tail:
    x,head = dequeue(Q,head)
    if x.time <= q:
        totime += x.time
        print(x.name + " " + str(totime))
    else:
        totime += q
        x.time -= q
        tail = enqueue(Q,x,tail)


