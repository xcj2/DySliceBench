import sys
INFTY=sys.maxsize
#INFTY=2*10**7+1

def readinput():
    nv,ne=list(map(int,input().split()))
    nMap=[]
    for i in range(nv):
        l=[]
        for _ in range(nv):
            l.append(INFTY)
        nMap.append(l)
        nMap[i][i]=0
    for _ in range(ne):
        s,t,d=list(map(int,input().split()))
        nMap[s][t]=d
    return nv,ne,nMap

def warshalFloyd(nv, nMap):
    for k in range(nv):
        for i in range(nv):
            if(nMap[i][k]==INFTY):
                continue
            for j in range(nv):
                if(nMap[k][j]==INFTY):
                    continue
                nMap[i][j] = min(nMap[i][j], nMap[i][k]+nMap[k][j])
    return nMap

def main(nv,ne,nMap):
    nMap=warshalFloyd(nv,nMap)
    #print(nMap)
    isNegative=False
    for i in range(nv):
        if nMap[i][i]<0:
            isNegative=True
    if isNegative==True:
        print('NEGATIVE CYCLE')
    else:
        for i in range(nv):
            for j in range(nv):
                #print(nMap[i][j],INFTY, nMap[i][j]==INFTY)
                if(nMap[i][j]==INFTY):
                    print('INF',end='')
                else:
                    print(nMap[i][j], end='')
                if j==nv-1:
                    print('')
                else:
                    print(' ',end='')
                        

if __name__=='__main__':
    nv,ne,nMap=readinput()
    #print(nMap)
    main(nv,ne,nMap)



