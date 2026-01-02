class myResi():
    def __init__(self):
        self.val=[[0]*10 for _ in range(3)]
    def __str__(self):
        ret = ''
        for i in range(3):
            ret += ' '+(str(self.val[i]).replace(',','')[1:10*2])+'\n'
        return ret.rstrip("\n")
    def setVal(self,f,r,v):
        self.val[f-1][r-1] += v
        
def fill(allb,b,f,r,v):
    bname=allb[b-1]
    bname.setVal(f,r,v)
    
b1=myResi()
b2=myResi()
b3=myResi()
b4=myResi()
allb=[b1,b2,b3,b4]
n=int(input())
for _ in range(n):
    b,f,r,v = map(int,input().split())
    fill(allb,b,f,r,v)
    
print(b1)
print('#'*20)
print(b2)
print('#'*20)
print(b3)
print('#'*20)
print(b4)