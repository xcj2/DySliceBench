import sys
sys.setrecursionlimit(1000000)
class Node:
    def __init__(self):
        self.next=[]
    def get_data(self,new_next,weight=1):
        self.next.append({new_next:weight})


def BFS():
    total=0
    check_node=tmp_node
    #print(check_node)
    now=min(check_node)
    tmp=[now]
    check_node.remove(now)
    ans=N-len(check_node)
    new_tmp=[]
    while len(check_node)>0:
        #print("tmp:{}".format(tmp))
        if tmp==[]:
            ans+=1
            tmp.append(check_node[0])
            check_node.remove(check_node[0])
        total+=1
        for each in tmp:
            #print("each:{}".format(each))
            for i in node[each].next:
                k=list(i.keys())[0]
                if k in check_node:
                    #print("append :{}".format(k))
                    new_tmp.append(k)
                    check_node.remove(k)
        #print("new_tmp:{}".format(new_tmp))
        #print("check_node:{}".format(check_node))
        tmp=new_tmp
        new_tmp=[]
    #print("end")
    #print("loop time:{}".format(total))
    #print("ans:{}".format(ans))
    print(ans)


def rec_BFS(i):
    tmp=[list(j.keys())[0] for j in i]
    for each in tmp:
        if not check_node[each]:
            check_node[each]=True
            rec_BFS(node[each].next)






        
        

N,M=list(map(int,input().split()))
node=[Node() for _ in range(N)]
#ans=[[100 for _ in range(N)]for _ in range(N)]
tmp_node=[]
for i in range(M):
    tmp_p,tmp_n,tmp_w=list(map(int,input().split()))
    #if not tmp_p-1 in tmp_node:
    #    tmp_node.append(tmp_p-1)
    #if not tmp_n-1 in tmp_node:
    #    tmp_node.append(tmp_n-1)
    node[tmp_p-1].get_data(tmp_n-1)
    node[tmp_n-1].get_data(tmp_p-1)
#BFS()
s=0
check_node=[False for _ in range(N)]
for i in range(N):
    if not check_node[i]:
        check_node[i]=True
        s+=1
        rec_BFS(node[i].next)
print(s)


