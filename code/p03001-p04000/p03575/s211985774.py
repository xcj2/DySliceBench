# ABC 075
def getInt(): return int(input())
def getIntList(): return [int(x) for x in input().split()]
def getIntFromRows(n): return [int(input()) for i in range(n)]
def getIntMat(n):
    mat = []
    for i in range(n): mat.append(getIntList())
    return mat
def zeros(n): return [0 for i in range(n)]
def zeros2(n, m): return [[0 for i in range(m)] for j in range(n)]

debug = True
def db(x): 
    if debug: print(x)

debug = False
n,m = getIntList()
a,b = zeros(m),zeros(m)
org = zeros(m)

for i in range(m):    org[i] = getIntList()

db(('org graph',org))
count = 0

def find(graph, fromNode, toNode, route): # -1: NG, >=OK、評価値
    db(('f-t',fromNode, toNode))
    if fromNode in route: return -1
    else:
        route = route + [fromNode]
        if fromNode==toNode: return 0
        for edge in graph:
            if edge[0]==fromNode:  # graphのソート、一旦fromが見つかった後の中断
                val = find(graph, edge[1], toNode, route)
                db(('found', route, edge[1], toNode))
                if val==0: return 0
        db(('cannot',fromNode, toNode))
        return -1
    
graph = zeros((m-1)*2)
count = 0
for i in range(m):
    new = org[:i] + org[i+1:]
    db(('cut',org[i]))
    db(('new',new))
    for j in range(m-1):
        graph[j*2] = new[j]
        graph[j*2+1] = [new[j][1], new[j][0]]
    graph.sort()
    db(('new graph',graph))
    route = []
    if find(graph, org[i][0], org[i][1], route)<0: count += 1
print(count)

def connected(graph, node): # 全ノードに行けるか
    db(('check node', node))
    for i in range(n):
        if i==node: continue
        found = False
        for e in graph:
            #db(('edge',e))
            if e[0]==node and e[1]==i: 
                found = True
                break
        if not found: return False
    db(('ok node', node))
    return True

