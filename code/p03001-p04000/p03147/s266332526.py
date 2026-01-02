import sys
import numpy as np
import collections

def parse(inp):
    N=int(next(inp))
    H=np.array(next(inp).split(),dtype=int)
    return H
  
def split(H):
    Splited=np.array([],dtype=int)
    SplitPoint=[]
    for i in range(len(H)):
        if(H[i]==0):
            SplitPoint.append(i)
    
    if(SplitPoint==[]):
        Splited=np.array([H])
        return Splited
            
    Splited=np.split(H,SplitPoint)
    
            
    
    for i in range(len(Splited)):
        if(Splited[i].size==0):
             continue
        elif(Splited[i][0]==0):
            Splited[i]=np.delete(Splited[i],[0])
    
    return Splited
                
def main(H):
    H=collections.deque(H)
#    print(H)

    answer=0
    
    while H:
        Hnow=H.popleft()
        if(Hnow.size==0):
            continue
#        print("now: ",Hnow)
        Hnowmin=Hnow.min()
        answer+=Hnowmin
        for i in range(len(Hnow)):
            Hnow[i]=Hnow[i]-Hnowmin
#        print("decreased: ",Hnow)
        for i in range(len(split(Hnow))):
            if(split(Hnow)[i].size!=0):
#                print("append: ",split(Hnow)[i])
                H.append(split(Hnow)[i])
#        print("H: ",H)
    return answer

print(main(split(parse(sys.stdin))))
