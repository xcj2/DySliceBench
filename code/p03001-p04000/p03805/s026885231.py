# ABC 054
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def zeros(n): return [0 for i in range(n)]
def zeros2(n, m): return [[0 for i in range(m)] for j in range(n)]

debug = True
def db(x): 
    if debug: print(x)

debug = False
N,m = getIntList()
org = zeros(m)

for i in range(m):    org[i] = getIntList()

db(('org graph',org))
Count = 0

def find(graph, fromNode, route): # -1: NG, >=OK、評価値
    global Count
    db(('find in',fromNode, route))
    if fromNode in route: return -1
    else:
        route = route + [fromNode]  # +=だとrouteを書き換えてしまう
        if len(route)==N: 
            db(('N',N))
            Count += 1
            return 0
        for edge in graph:
            if edge[0]==fromNode:  # graphのソート、一旦fromが見つかった後の中断
                val = find(graph, edge[1], route)
                #if val==0: 
                #    db(('found', route, edge[1]))
                #    return 0
        #db(('cannot',fromNode))
        return -1
    
graph = zeros(m*2)
for i in range(m):
    graph[i*2] = org[i]
    graph[i*2+1] = [org[i][1], org[i][0]]
graph.sort()
db(('new graph',graph))
route = []
find(graph, 1, route)
print(Count)

