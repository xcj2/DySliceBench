from collections import deque

UNVISITED=0
ENTERED=1
VISITED=2

def nextNL(u, nList, state):
    l=nList[u]
    for i in l:
        if(state[i]==UNVISITED):
            return i
    return -1

def dfs(s,t,nList,state, color,icol):

    S=[]

    S.append(s)
    state[s]=ENTERED
    color[s]=icol
    while(len(S)>0):
        current=S[-1]
        next=nextNL(current, nList, state)
        if next!=-1:
            S.append(next)
            state[next]=ENTERED
            color[next]=icol
        else:
            state[S.pop()]=VISITED

    return color[s]==color[t]

def main():

    n,m=list(map(int,input().split()))
    nList=[]
    for _ in range(n):
        nList.append([])

    for _ in range(m):
        s,t=list(map(int,input().split()))
        nList[s].append(t)
        nList[t].append(s)
    
    state=[UNVISITED]*n

    q=int(input())

    icol=-1
    color=[icol]*n
    for _ in range(q):
        s,t=list(map(int,input().split()))
        if(color[s] == -1) and (color[t] == -1):
            icol+=1
            res=dfs(s,t,nList,state,color,icol)
            if(res==True):
                print('yes')
            else:
                print('no')
        elif (color[s]==-1) or (color[t]==-1):
            print('no')
        elif (color[s] == color[t]):
            print('yes')
        else:
            print('no')
    
if __name__=='__main__':
    main()


    


