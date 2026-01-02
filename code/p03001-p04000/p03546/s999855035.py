
import queue
from heapq import heappush, heappop

class Graph:

    INF = float('inf')
    
    def __init__(self,v_num,is_directed = False):
        self.is_directed = is_directed
        self.v_num = v_num
        self.E = []
        self.v_s_list = [[] for i in range(self.v_num)]
        
    def appendEdge(self,v1,v2,weight=1):
        if max(v1,v2,self.v_num-1)>=self.v_num or min(v1,v2)<0:
            print("ERROR: The vertex ID is wrong.")
            return False

        self.E.append([v1,v2,weight])
        
        if self.is_directed:
            self.v_s_list[v1].append([v2,weight])
        else:
            self.v_s_list[v1].append([v2,weight])
            self.v_s_list[v2].append([v1,weight])
        
        
    def BFS(self,v,usage="SSSP"):
        is_processed = [False for i in range(self.v_num)]
        distance_list = [Graph.INF for i in range(self.v_num)]
        Q = queue.Queue()
        Q.put(v)
        is_processed[v]=True
        distance_list[v] = 0
        while not Q.empty():
            v1 = Q.get()
            for v2 in self.v_s_list[v1]:
                if not is_processed[v2[0]]:
                    is_processed[v2[0]] = True
                    distance_list[v2[0]] = min(distance_list[v1]+1,distance_list[v2[0]])
                    Q.put(v2[0])
        if usage=="SSSP":
            return distance_list
        elif usage=="ConnectedComponent":
            cc_list = []
            for i in range(self.v_num):
                if is_processed[i]:
                    cc_list.append(i)
            return cc_list

    def getSSSPwithBFS(self,v):
        return self.BFS(v,"SSSP")
        
    def getConnectedComponent(self,v):
        return self.BFS(v,"ConnectedComponent")
        
    def getSSSPwithBellmanFord(self,v):
        distance_list = [Graph.INF for i in range(self.v_num)]
        distance_list[v] = 0
        pre_list = [None for i in range(self.v_num)]

        for i in range(self.v_num-1):
            for e in self.E:
                v1 = e[0]
                v2 = e[1]
                d = e[2]
                if distance_list[v2] > distance_list[v1] + d:
                    distance_list[v2] = distance_list[v1] + d
                    pre_list[v2] = v1
                    
        negative_loop_list = [False for i in range(self.v_num)]
        
        for i in range(self.v_num):
            for e in self.E:
                v1 = e[0]
                v2 = e[1]
                d = e[2]
                if d + distance_list[v1] < distance_list[v2]:
                    distance_list[v2] = d + distance_list[v1]
                    pre_list[v2] = v1
                    negative_loop_list[v2] = True
        
        return distance_list, pre_list, negative_loop_list

    def getSSSPwithDijkstra(self,v):
        distance_list = [Graph.INF for i in range(self.v_num)]
        distance_list[v] = 0
        pre_list = [None for i in range(self.v_num)]
        
        PQ = []
        for i in range(self.v_num):
            heappush(PQ,(distance_list[i],i))
        while len(PQ)>0:
            d,v1 = heappop(PQ)
            for v2 in self.v_s_list[v1]:
                if distance_list[v2[0]] > d + v2[1]:
                    distance_list[v2[0]] = d + v2[1]
                    pre_list[v2[0]] = v1
                    heappush(PQ,(distance_list[v2[0]],v2[0]))
        return distance_list,pre_list
    
H,W=list(map(int,input().split()))
C = []
for i in range(10):
    C.append(list(map(int,input().split())))

G = Graph(10,True)

for i in range(10):
    for j in range(10):
        if i!=j:
            G.appendEdge(i,j,C[i][j])

dto1 = []
for i in range(10):
    distance_list, pre_list, negative_loop_list=G.getSSSPwithBellmanFord(i)
    dto1.append(distance_list[1])
cost = 0
for i in range(H):
    A = list(map(int,input().split()))
    for j in range(W):
        if A[j]!=-1:
            cost+=dto1[A[j]]
            
print(cost)