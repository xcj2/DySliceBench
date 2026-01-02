class proc:
    def __init__(self, id, val):
        self.id=id
        self.val=int(val)

class queue:

    def __init__(self, n, datas):
        self.max=n*2
        self.head=0
        self.tail=0
        #print("n="+str(n))

        self.q=[None for _ in range(self.max)]
        for d in datas:
            p=proc(d[0],int(d[1]))
            self.enque(p)
            #print(self.tail)

        #print(self.tail)



    def enque(self,p):
        self.q[self.tail]=p
        self.tail=(self.tail+1)%self.max

    def deque(self):
        x=self.q[self.head]
        self.head=(self.head+1)%self.max
        return x

n, sec =map(int, input().split())
datas=[]
for i in range(n):
    datas.append(input().split())

q=queue(n,datas)
total=0
while(q.head !=q.tail):
    top=q.deque()
    usage=min(top.val, sec)
    total=total+usage
    top.val=top.val-usage
    if(top.val > 0):
        q.enque(top)
    else:
        print(top.id+" "+str(total))






