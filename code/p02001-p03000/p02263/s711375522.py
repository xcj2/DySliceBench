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
    
    def set_nex(self,n):self.__nex=n
    
    def set_val(self,n):self.__val=n
    
    def get_val(self):return self.__val

class Stack:
    member=Trio(None)
    def __init__(self,stri):
        if(isinstance(stri,str)):
            for i,e in enumerate(stri):
                if(i==0):
                    self.member.set_val(e)
                else:
                    self.push(e)

    
    def push(self,n):
        self.member.set_nex(Trio(n,self.member,None))
        self.member=self.member.get_nex()

    def pop(self):
        if(self.member==None):
            return None
        d=self.member.get_val()
        self.member=self.member.get_pre()
        return d

s=input()
stk = Stack(None)
stri=""
for i in s:
    if(i==" "):
        stk.push(stri)
        stri=""
    elif(i.isdigit()):
        stri="".join([stri,i])
    elif(i=="+" or i=="-" or i=="*"):
        b=stk.pop()
        b=int(b)
        a=int(stk.pop())
        if(i=="+"):
            stri=(str(a+b))
        elif(i=="-"):
            stri=(str(a-b))
        else:
            stri=(str(a*b))

print(stri)