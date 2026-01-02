#電球クラス
class Light:
    def __init__(self,name,switchs,whattype):
        self.name=name
        self.switchs=switchs
        self.whattype=whattype
    def reset(self):
        sumnum=0
        for switch in self.switchs:
            sumnum+=switch.onoff
        if sumnum%2==self.whattype:
            self.state="on"
        else:
            self.state="off"
            
#スイッチクラス            
class Switch:
    def __init__(self,name):
        self.name=name
        self.onoff=0
    def click(self,onoff):
        self.onoff=onoff
        
    
#整理用データ
n,m=[int(i) for i in input().split()]
allist=[]
for i in range(m+1):
    allist.append([int(j) for j in input().split()])
      

#全スイッチのリスト
switchlist=[]
for i in range(n):
    switchlist.append(Switch(i))


#全電球のリスト
lightlist=[]
for i in range(m):
    swlist=[]
    swnum=allist[i][1:]
    for j in swnum:
        swlist.append(switchlist[j-1])
    whattype=allist[-1][i]
    lightlist.append(Light(i,swlist,whattype))
    
#全部の付け方について
count=0
clicklist=[0 for i in range(n)]    
for i in range(2**n):
    onoffcheck=0
    j=0
    while i:
        clicklist[j]=i%2
        i=i//2
        j+=1
    for k in range(n):
        switchlist[k].click(clicklist[k])
    for light in lightlist:
        light.reset()
        if light.state=="off":
            onoffcheck+=1
    if onoffcheck==0:
        count+=1
print(count)