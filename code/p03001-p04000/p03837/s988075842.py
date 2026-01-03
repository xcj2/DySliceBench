
def dijkstra(graph,weight,s,N):
    distance=[1e10 for i in range(N)]
    distance[s]=0
    unvisited=[i for i in range(N)]
    while len(unvisited)>0:
        unvisited.sort(key=lambda x:distance[x])
        v=unvisited.pop(0)
        for w in graph[v]:
            if distance[w]>distance[v]+weight[(v,w)]:
                distance[w] = distance[v] + weight[(v, w)]
    return distance

def e_check(e,d_list,weight,N):
    for i in range(N):
        for j in range(N):
            if e[0]!=i and e[1]!=j and d_list[e[0]][i]+weight[(i,j)]==d_list[j][e[1]]:
                return True
    return False

def e_check_2(E,d_list,weight):
    count=0
    for e in E:
        if d_list[e[0]][e[1]]!=weight[e]:
            count+=1
    return count


if __name__ == '__main__':
    N,M=list(map(int,input().split()))
    graph={i:[] for i in range(N)}
    weight={(i,j):1e10 for i in range(N) for j in range(N)}
    E=[]

    for i in range(M):
        a,b,c = list(map(int, input().split()))
        E.append((a-1,b-1))
        E.append((b-1,a-1))
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
        weight[(a-1,b-1)]=c
        weight[(b-1,a-1)]=c
    d_list={i:dijkstra(graph,weight,i,N) for i in range(N)}

    ans=e_check_2(E,d_list,weight)

    print(ans//2)