import copy
from collections import deque

H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]


def check(tup):
    global H
    global W
    global S

    tup_x=tup[0]
    tup_y=tup[1]
    if 0<=tup_x<H and 0<=tup_y<W:
        if S[tup_x][tup_y]=='.':
            return True
    else:
        return False

def neighbor(tup):
    x=tup[0]
    y=tup[1]
    cand=[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    List=[]
    for c in cand:
        if check(c):
            List.append(c)
    return List

def bfs(start):#startはtuple型
    global H
    global W

    if check(start):
        deq=deque()#as queue
        Dict=[]
        component=[]
        for i in range(W):
            component.append(-1)
        for j in range(H):
            Dict.append(copy.copy(component))

        deq.append(start)
        Dict[start[0]][start[1]]=0
        while deq:
            now=deq.popleft()
            nexts=neighbor(now)
            for next in nexts:
                next_x=next[0]
                next_y=next[1]
                if Dict[next_x][next_y]>=0:
                    continue
                #if next in deq:
                    #continue
                deq.append(next)
                Dict[next_x][next_y]=Dict[now[0]][now[1]]+1

        M=[]
        for d in Dict:
            M.append(max(d))
        return max(M)
    
    else:
        return 0

Ans=[]
for k in range(H):
    for l in range(W):
        Ans.append(bfs((k,l)))

print(max(Ans))


