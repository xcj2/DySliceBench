import heapq
import sys
input = sys.stdin.readline

n = int(input())
x_list, y_list = [], []
for i in range(n):
    a, b = [ int(v) for v in input().split() ]
    x_list.append((a,b))
    y_list.append((b,a))
x_list.sort()
y_list.sort()

def swap(i):
    return (i[1],i[0])

def simplehash(i, r = 0):
    if r == 1:
        a, b = swap(i)
    else:
        a, b = i
    return a*10**10+b

x_node = [ ( (x_list[i+1][0] - x_list[i][0]), simplehash(x_list[i]), simplehash(x_list[i+1]) ) for i in range(n-1) ]
y_node = [ ( (y_list[i+1][0] - y_list[i][0]), simplehash(y_list[i],1), simplehash(y_list[i+1],1) ) for i in range(n-1) ]
node_set = set([])
for i in x_node:
    node_set.add(i[1])
    node_set.add(i[2])
node = list(sorted(node_set))
node_dic = { v : i for i, v in enumerate(node) }

x_list = [ (i[0], node_dic[i[1]], node_dic[i[2]] ) for i in x_node ]
y_list = [ (i[0], node_dic[i[1]], node_dic[i[2]] ) for i in y_node ]

connect_list = [ set([]) for i in range(n) ]
for i in x_list + y_list:
    c, a, b = i
    connect_list[a].add((c,b))
    connect_list[b].add((c,a))

def prim(in_connect_list,p,m):
    total_cost = 0
    connected_node = [ 0 for i in range(m) ]
    connected_node[p] = 1
    search_list = [p]
    search_heap = []
    while search_list != []:
        new_search_list = []
        for i in search_list:
            for c, k in connect_list[i]:
                if connected_node[k] == 0:
                    heapq.heappush(search_heap,(c,k))
          
        while search_heap != []:
            c, k = heapq.heappop(search_heap)
            if connected_node[k] == 0:
                new_search_list = [k]
                connected_node[k] = 1
                total_cost += c
                break
        search_list = new_search_list
    return total_cost

print(prim(connect_list,0,n))