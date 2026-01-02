class Trio:
    __pre=None
    __val=None
    __nex=None
    def __init__(self,val,p=None,n=None):
        self.__pre=p
        self.__val=val
        self.__nex=n
    
    def get_pre(self):return self.__pre
    
    def get_nex(self):return self.__nex
    
    def set_pre(self,n):self.__pre=n
        
    def set_nex(self,n):self.__nex=n
    
    def set_val(self,n):self.__val=n
    
    def get_val(self):return self.__val
    
class Queue:
    top = back = None
    def __init__(self):
        pass
    
    def enqueue(self,n):
        if(self.top==None):
            self.top = self.back = Trio(n)
        else:
            self.back.set_nex(Trio(n,p=self.back))
            self.back=self.back.get_nex()
    
    def dequeue(self):
        if(self.top==None):
            return None
        elif(self.top==self.back):
            a=self.top.get_val()
            self.top,self.back=None,None
            return a
        else:
            self.top=self.top.get_nex()
            oldtop=self.top.get_pre()
            self.top.set_pre(None)
            return oldtop.get_val()

s = input()
n,limit=map(int,s.split())
que=Queue()
for i in range(n):
    lis=input().split()
    que.enqueue((lis[0],int(lis[1])))

time=0
while(True):
    elm=que.dequeue()
    if(elm==None):
        break
    elif(elm[1]>limit):
        que.enqueue((elm[0],elm[1]-limit))
        time+=limit
    else:
        time+=elm[1]
        print(elm[0],time)